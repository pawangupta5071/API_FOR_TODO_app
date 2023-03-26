from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.


@api_view(["GET"])
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'message': 'Item Not found'}, status=404)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def todo_create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["PUT"])
def todo_update(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'message': 'Item Not found'}, status=404)

    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def todo_delete(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response("todo does not exist", status=status.HTTP_404_NOT_FOUND)

    todo.delete()
    return Response("ITEM succesfully deleted", status=status.HTTP_204_NO_CONTENT)
