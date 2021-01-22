
import graphene
from graphene_django.types import DjangoObjectType
from posts.models import Article


class ArticleType(DjangoObjectType):

    class Meta:
        model = Article


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType, title=graphene.String)

    def resolve_articles(self, info, **kwargs):
        title = kwargs.get('title')
        if title is not None:
            return Article.Objects.filter(title_contains=title)
        return Article.objects.all()
