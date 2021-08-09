import graphene
from todo_list.schema import Query, Mutation


schema = graphene.Schema(query=Query, mutation=Mutation)
