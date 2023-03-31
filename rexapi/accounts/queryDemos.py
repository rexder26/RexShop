
customers = Customer.objects.all()
firstCustomer = Customer.objects.first()
#(3) Returns last customer in table
lastCustomer = Customer.objects.last()
#(4) Returns single customer by name
customerByName = Customer.objects.get(name='Peter Piper')
#***(5) Returns single customer by name
customerById = Customer.objects.get(id=4)
#***(6) Returns all orders related to customer (first Customer variable set above)
firstCustomer.order_set.all()
#(7) ***Returns orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name
#(8) ***Returns products from products table with value of "Out Door" in category attribute
products = Product.objects.filter(category="Out Door")
#(9) ***Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')
# (10) Returns all products with tag of "Sports": (Query Many to Many Fields)
products Filtered = Product.objects.filter (tags_name="Sports")

#Returns the total count for number of time a "Ball
ballOrders = first Customer.order_set.filter (product_na
#Returns total count for each product orderd
allOrders = {}
for order in firstCustomer.order_set.all():
if order.product.name in allOrders:
allOrders [order.product.name] += 1
else:
allOrders [order.product.name] = 1
#Returns: allorders: {'Ball': 2, 'BBQ Grill': 1}
#RELATED SET EXAMPLE
class ParentModel(models.Model):
name = models. CharField (max_length=200, null=True