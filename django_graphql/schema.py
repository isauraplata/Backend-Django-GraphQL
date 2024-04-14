import graphene
from graphene_django import DjangoObjectType 
from products.models import Product, Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "selling_price", "purchase_price", "category", "available_quantity", "created_at", "updated_at")

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class CreateProductMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        selling_price = graphene.Decimal()
        purchase_price = graphene.Decimal()
        category_id = graphene.Int()
        available_quantity = graphene.Int()

    product = graphene.Field(ProductType)

    def mutate(self, info, name, description, selling_price, purchase_price, category_id, available_quantity):
        category = Category.objects.get(pk=category_id)
        product = Product(
            name=name,
            description=description,
            selling_price=selling_price,
            purchase_price=purchase_price,
            category=category,
            available_quantity=available_quantity
        )
        product.save()
        return CreateProductMutation(product=product)

class DeleteProductMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        product = Product.objects.get(pk=id)
        product.delete()
        return DeleteProductMutation(message="Product deleted")

class UpdateProductMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()
        selling_price = graphene.Decimal()
        purchase_price = graphene.Decimal()
        category_id = graphene.Int()
        available_quantity = graphene.Int()

    product = graphene.Field(ProductType)

    def mutate(self, info, id, name=None, description=None, selling_price=None, purchase_price=None, category_id=None, available_quantity=None):
        product = Product.objects.get(pk=id)
        if name:
            product.name = name
        if description:
            product.description = description
        if selling_price:
            product.selling_price = selling_price
        if purchase_price:
            product.purchase_price = purchase_price
        if category_id:
            category = Category.objects.get(pk=category_id)
            product.category = category
        if available_quantity:
            product.available_quantity = available_quantity
        product.save()
        return UpdateProductMutation(product=product)

class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, description=None):
        category = Category(name=name, description=description)
        category.save()
        return CreateCategoryMutation(category=category)

class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        category = Category.objects.get(pk=id)
        category.delete()
        return DeleteCategoryMutation(message="Category deleted")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello!")
    products = graphene.List(ProductType)
    product = graphene.Field(ProductType, id=graphene.ID(required=True))

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_product(self, info, id):
        return Product.objects.get(pk=id)

class Mutation(graphene.ObjectType):
    create_product = CreateProductMutation.Field()
    delete_product = DeleteProductMutation.Field()
    update_product = UpdateProductMutation.Field()
    create_category = CreateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
