# 总的schema的入口

import graphene
import book.schema


class Query(book.schema.Query, graphene.ObjectType):
    # 总的schema的query入口
    pass


class Mutations(graphene.ObjectType):
    # 总的schema的mutations入口
    create_book = book.schema.CreateBook.Field()


schema = graphene.Schema(query=Query)

# , mutation=Mutations