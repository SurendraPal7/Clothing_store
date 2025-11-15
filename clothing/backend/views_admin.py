from django.shortcuts import render

def sales_dashboard(request):
    return render(request, 'admin/dashboard.html')  # you can change template path
