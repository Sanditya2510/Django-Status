from rest_framework import generics,mixins,permissions
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from status.models import Status 
from rest_framework.authentication import SessionAuthentication
from .serializers import StatusSerializer
from rest_framework.response import Response 
from accounts.api.permissions import IsOwnerOrReadOnly

# class StatusListSearchAPIView(APIView):
#     permission_classes              = []
#     authentication_classes          = []
    
    # def get(self,request,format=None):
    #     qs = Status.objects.all()
    #     serializer = StatusSerializer(qs,many=True)
    #     return Response(serializer.data)

#     def post(self,request,format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs,many=True)
#         return Response(serializer.data)

# class StatusAPIView(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     # mixins.UpdateModelMixin,
#                     # mixins.DestroyModelMixin,
#                     generics.ListAPIView):
#     permission_classes              = []
#     authentication_classes          = []
#     serializer_class = StatusSerializer

#     def get_queryset(self):
#         request = self.request
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

#     def get_object(self):
#         request = self.request
#         passed_id = request.GET.get('id',None)
#         queryset = self.get_queryset()
#         if passed_id is not None:
#             obj = get_object_or_404(queryset,id=passed_id)  
#             self.check_object_permissions(request, obj)
#         return obj
    
#     def get(self,request,*args,**kwargs):
#         passed_id = request.GET.get('id',None)
#         if passed_id is not None:
#             return self.retrieve(request,*args,**kwargs)
#         return super().get(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         requested_id = request.data.get('id')
#         return self.update(request,*args,**kwargs)

#     def patch(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


class StatusDetailAPIView(  mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    # lookup_field = 'id'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self,update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)  



class StatusAPIView(mixins.CreateModelMixin,
                        generics.ListAPIView):
        permission_classes              = [permissions.IsAuthenticatedOrReadOnly]
        # authentication_classes          = [SessionAuthentication]
        serializer_class = StatusSerializer
        

        def get_queryset(self):
            request = self.request
            print(request.user)
            qs = Status.objects.all()
            query = self.request.GET.get('q')
            if query is not None:
                qs = qs.filter(content__icontains=query)
            return qs

        def post(self,request,*args,**kwargs):
            return self.create(request,*args,**kwargs)

        def perform_create(self,serializer):
            serializer.save(user=self.request.user)

        # def get(self,request,format=None):
        #     qs = Status.objects.all()
        #     serializer = StatusSerializer(qs,many=True)
        #     return Response(serializer.data)

    # def get_object(self,*args,**kwargs):
    #     kwargs = self.kwargs, 
    #     kw_id = kwargs.get('abc')
    #     return Status.objects.get(id=kw_id)

# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer 

# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer 