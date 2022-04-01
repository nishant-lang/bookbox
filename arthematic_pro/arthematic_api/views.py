from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    """Showing all the links which are Avilable"""
    api_urls={
        'list':'Arthematic_oprations',
        'Add':'/api/add/<int:num1>/<int:num2>',
        'Sub':'/api/sub/<int:num1>/<int:num2>',
        'Mul':'/api/mul/<int:num1>/<int:num2>',
        'Div':'/api/div/<int:num1>/<int:num2>',
        
    }
    return Response (api_urls)

@api_view(['GET'])
def add(request,num1,num2):
    """Adding two number"""
    
    return Response ({'Add':f'The sum of the {num1} and {num2} is {num1+num2}'})

@api_view(['GET'])
def sub(request,num1,num2):
    """Subtracting two number"""
    
    return Response ({'Sub':f'The subtract of the {num1} and {num2} is {num1-num2}'})

@api_view(['GET'])
def mul(request,num1,num2):
    """Multiplication of two number"""
    
    return Response ({'Mul':f'The multiplication of the {num1} and {num2} is {num1*num2}'})

@api_view(['GET'])
def div(request,num1,num2):
    """Divison of two numbers"""
    
    return Response ({'Div':f'The Division of the {num1} and {num2} is {num1/num2}'})

