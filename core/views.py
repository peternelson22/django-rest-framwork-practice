from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets
from rest_framework import status   
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import ArticleSerializer
from .models import Article

###### Using APIView #########
class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ArticleCreate(APIView):
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleSingle(APIView):
   
    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response({'error': 'Article does not exist'},status=status.HTTP_404_NOT_FOUND)
    
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response({'message':'Successfully deleted'}, status=status.HTTP_204_NO_CONTENT)


####### USING GENERICVIEW AND MIXINS ###########

class ArticleGenericView(generics.GenericAPIView, mixins.ListModelMixin, 
                        mixins.CreateModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication] For SessionBase or BasicAuthBase
    authentication_classes = [TokenAuthentication] # For TokenBase Auth
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

  
class ArticleEditGenericView(generics.GenericAPIView, mixins.UpdateModelMixin, 
                            mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    lookup_field = 'pk'
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

#### USING VIEWSETS ######

class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response({'message':'Successfully deleted'}, status=status.HTTP_204_NO_CONTENT)

###### Using GenericViewSet #######

class ArticleGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

###### Using ModelViewSet ######

class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

