from flask import Flask, redirect
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Int, List, Field, Schema, Mutation

# Estructura de un usuario
class User(ObjectType):
    id = Int()
    name = String()
    email = String()

# Base de datos en memoria
users_data = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Consultas
class Query(ObjectType):
    users = List(User)

    def resolve_users(self, info):
        return users_data

# Mutaciones
class CreateUser(Mutation):
    class Arguments:
        id = Int(required=True)
        name = String(required=True)
        email = String(required=True)

    user = Field(User)

    def mutate(self, info, id, name, email):
        new_user = {"id": id, "name": name, "email": email}
        users_data.append(new_user)
        return CreateUser(user=new_user)

class Mutation(ObjectType):
    create_user = CreateUser.Field()

# Configuración del esquema de GraphQL
schema = Schema(query=Query, mutation=Mutation)

# Configuración del servidor Flask
app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

# Redirección de la raíz '/' a '/graphql'
@app.route('/')
def index():
    return redirect('/graphql')

# Debugging adicional para imprimir las rutas disponibles
if __name__ == '__main__':
    print("Rutas disponibles:")
    print(app.url_map)  # Imprime el mapa de rutas registradas
    app.run(debug=True, port=5000)