from django.shortcuts import render
from django.views import View
from django import http

from goods.models import GoodsCategory
from contents.utils import get_categories


class ListView(View):
    """商品列表页"""

    def get(self, request, category_id, page_num):
        """提供商品列表页"""
        # 判断category_id是否正确
        try:
            category = GoodsCategory.objects.get(id=category_id)
        except GoodsCategory.DoesNotExist:
            return http.HttpResponseNotFound('GoodsCategory does not exist')

        # 查询商品频道分类
        categories = get_categories()

        # 渲染页面
        context = {
            'categories':categories,
        }
        return render(request, 'list.html', context)