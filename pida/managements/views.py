from django.shortcuts import render
from rest_framework import generics, renderers, views
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Notice, Faq, Agreement
from .serializers import NoticeSerializer, FaqSerializer, AgreementSerializer


class NoticeList(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class NoticeDetail(generics.RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class FaqList(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqDetail(generics.RetrieveAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class AgreementList(generics.ListAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('visible',)


class AgreementDetail(generics.RetrieveAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer


class AgreementPlain(views.APIView):
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        agreements = Agreement.objects.filter(visible=True)
        data = "\n\n".join(["%s\n%s"%(a.title, a.content) for a in agreements])
        return Response(data)
