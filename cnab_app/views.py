from cnab_app.models import Cnab

from cnab_app.serializers import CnabSerializer, FileSerializer

from rest_framework.views import APIView, Response, status


class CnabView(APIView):
    serializer_class = FileSerializer

    def get(self, request):
        listTransctions = Cnab.objects.all()

        serializer = CnabSerializer(listTransctions, many=True)

        return Response(serializer.data)

    def post(self, request):
        list_transaction = []

        file = request.FILES.get("file")

        for tran in file:

            tab = {
                "type": int(tran[:1].decode("utf-8")),
                "data": f"{tran[1:5].decode('utf-8')}-{tran[5:7].decode('utf-8')}-{tran[7:9].decode('utf-8')}",
                "valor": int(tran[9:19].decode("utf-8")) / 100,
                "cpf": tran[19:30].decode("utf-8"),
                "cartao": tran[30:42].decode("utf-8"),
                "hora": f'{tran[42:44].decode("utf-8")}:{tran[44:46].decode("utf-8")}:{tran[46:48].decode("utf-8")}',
                "dono": tran[48:62].decode("utf-8"),
                "loja": tran[62:].decode("utf-8"),
            }

            serializer = CnabSerializer(data=tab)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            list_transaction.append(serializer.data)

        return Response(list_transaction, status.HTTP_201_CREATED)


class SearchMovementOfOneStoreView(APIView):
    def get(self, request):
        store = request.query_params.get("loja", None)

        store = Cnab.objects.filter(loja__icontains=store)

        serializer = CnabSerializer(store, many=True)

        count = 0

        for move in serializer.data:
            if dict(move)['type'] == 2 or dict(move)['type'] == 3 or dict(move)['type'] == 9:
                count -= float(dict(move)['valor'])
            else:
                count += float(dict(move)['valor'])

        data_of_returning = {
            "Account_balance": round(count, 2),
            "store_trasation_history": serializer.data
        }

        return Response(data_of_returning)
