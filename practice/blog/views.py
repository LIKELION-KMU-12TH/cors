from django.shortcuts import render

from .models import Blog
from .serializer import BlogSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BlogListAPIView(APIView):
    # 블로그 리스트 조회
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 블로그 작성
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailAPIView(APIView):
    def get_object(self, blog_id):
        return Blog.objects.get(id=blog_id)

    # 블로그 상세 조회
    def get(self, request, blog_id):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 블로그 수정
    def put(self, request, blog_id):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 블로그 삭제
    def delete(self, request, blog_id):
        blog = self.get_object(blog_id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)