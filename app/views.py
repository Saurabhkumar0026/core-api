import json

from django.shortcuts import render

from .models import Student
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def all_data(req):
    if req.method=='POST':
        data=req.body
        print(data)
        print(type(data))
        p_data=json.loads(data)
        print(p_data)
        print(type(p_data))
        n=p_data.get('name')
        a=p_data.get('age')
        e=p_data.get('email')
        c=p_data.get('contact')
        if  'name' in p_data and 'age' in p_data and 'email' in p_data and 'contact' in p_data:
            Student.objects.create(name=n,age=a,email=e,contact=c)
            p_data={"msg":"objects created"}
            return HttpResponse(json.dumps(p_data),content_type='application/json')
        else:
            if not 'name' in p_data:
                p_data={"msg":"name is required"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            if not 'age' in p_data:
                p_data={"msg":"age is required"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            
            if not 'email' in p_data:
                p_data={"msg":"email is required"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            
            if not 'contact' in p_data:
                p_data={"msg":"contact is required"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
        return HttpResponse(json.dumps(p_data),content_type='application/json')
        
        

            

    data=Student.objects.all()
    print(data)
    p_data=list(data.values())
    print(p_data)
    j_data=json.dumps(p_data)
    print(j_data)
    return HttpResponse(j_data,content_type='application/json')

@csrf_exempt
def single_data(req,pk):
    user = Student.objects.filter(id=pk)
    if not user:
        p_data={"msg":"Enter id not present in oyr db"}
        return HttpResponse(json.dumps(p_data),content_type='application/json')
    else:
        if req.method == 'PUT':
            data=req.body
            print(data)
            print(type(data))
            p_data=json.loads(data)
            print(p_data)
            print(type(p_data))
            if  'name' in p_data and 'age' in p_data and 'email' in p_data and 'contact' in p_data:
                a=p_data.get('age')
                e=p_data.get('email')
                n=p_data.get('name')
                c=p_data.get('contact')
                old_data=Student.objects.get(id=pk)
                old_data.name=n
                old_data.age=a
                old_data.email=e
                old_data.contact=c
                old_data.save()
                p_data={"msg":"object updated"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            else:
                if not 'name' in p_data:
                    p_data={"msg":"name is required"}
                    return HttpResponse(json.dumps(p_data),content_type='application/json')
                if not 'age' in p_data:
                    p_data={"msg":"age is required"}
                    return HttpResponse(json.dumps(p_data),content_type='application/json')
            
                if not 'email' in p_data:
                    p_data={"msg":"email is required"}
                    return HttpResponse(json.dumps(p_data),content_type='application/json')
                
                if not 'contact' in p_data:
                    p_data={"msg":"contact is required"}
                    return HttpResponse(json.dumps(p_data),content_type='application/json')
        elif req.method=='PATCH':
            data=req.body
            print(data)
            print(type(data))
            p_data=json.loads(data)
            print(p_data)
            print(type(p_data))
            n=p_data.get("name")
            a=p_data.get("age")
            c=p_data.get("contact")
            e=p_data.get("email")
            if p_data:
                n=p_data.get("name")
                a=p_data.get("age")
                c=p_data.get("contact")
                e=p_data.get("email")
                old_data=Student.objects.get(id=pk)
                if n:
                    old_data.name=n
                if a:
                    old_data.age=a
                if c:
                    old_data.contact=c
                if e:
                    old_data.email=e
                old_data.save()
                p_data={"msg":"Data partially updated"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            else:
                p_data={"msg":"Object values are missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            
        elif req.method=='DELETE':
            user=Student.objects.get(id=pk)
            user.delete()
            p_data={"msg":"Data deleted"}
            return HttpResponse(json.dumps(p_data),content_type='application/json')        


                


        

    
        data=Student.objects.get(id=pk)
        print(data)
        print(type(data))
        p_data=model_to_dict(data)
        print(p_data)
        print(type(p_data))
        j_data=json.dumps(p_data)
        print(j_data)
        return HttpResponse(j_data,content_type='application/json')
        
    



    
                      
