from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from firma.models import *


def homePageView(request):
    employee = Employee.objects.all()
    departments = Departments.objects.all()
    education = Education.objects.all()
    passports = Pasports.objects.all()
    timetable = Timetable.objects.all()
    employee_cols = ["Номер", "Имя", "Фамилия", "Отчество", "Пол", "Дата рождения", "Адрес", "Телефон",
                     "Номер должности"]
    departments_cols = ["Номер", "Имя"]
    education_cols = ["Номер образования", "Номер сотрудника", "Тип", "Имя"]
    passports_cols = ["id", "Номер сотрудника", "Номер паспорта", "Кем выдан", "Дата"]
    timetable_cols = ["Номер должности", "Номер отдела", "Название", "Кол-во"]
    data = {"employee_cols": employee_cols, "departments_cols": departments_cols, "education_cols": education_cols,
            "passports_cols": passports_cols, "timetable_cols": timetable_cols, "employee": employee,
            "departments": departments, "education": education, "passports": passports, "timetable": timetable}
    return render(request, 'index.html', data)


def searchPageView(request, name):
    atr = request.POST.get("atr")
    req = request.POST.get("request")
    radio_dict = {
        "employee": ["Номер", "Имя", "Фамилия", "Отчество", "Пол", "Дата рождения", "Адрес", "Телефон",
                     "Номер должности"],
        "departments": ["Номер", "Имя"],
        "education": ["Номер образования", "Номер сотрудника", "Тип", "Имя"],
        "passports": ["id", "Номер сотрудника", "Номер паспорта", "Кем выдан", "Дата"],
        "timetable": ["Номер должности", "Номер отдела", "Название", "Кол-во"]
    }
    if name == "employee":
        employee = Employee.objects.get
        if atr == "Номер":
            employee = Employee.objects.filter(id=req).all()
            data = {"radio": radio_dict.get(name), "dict": employee, "employee": True}
            return render(request, 'search_extends.html', data)
        if atr == "Имя":
            employee = Employee.objects.filter(first_name=req).all()
            data = {"radio": radio_dict.get(name), "dict": employee, "employee": True}
            return render(request, 'search_extends.html', data)
        if atr == "Фамилия":
            employee = Employee.objects.filter(last_name=req).all()
            data = {"radio": radio_dict.get(name), "dict": employee, "employee": True}
            return render(request, 'search_extends.html', data)
        if atr == "Отчество":
            employee = Employee.objects.filter(patronymic=req).all()
            data = {"radio": radio_dict.get(name), "dict": employee, "employee": True}
            return render(request, 'search_extends.html', data)
        if atr == "Пол":
            employee = Employee.objects.filter(pol=req).all()
            data = {"radio": radio_dict.get(name), "dict": employee, "employee": True}
            return render(request, 'search_extends.html', data)
        if atr == "Дата рождения":
            employee = Employee.objects.filter(date=req).all()
            data = {"radio": radio_dict.get(name), "dict": employee, "employee": True}
            return render(request, 'search_extends.html', data)
        if atr == "Адрес":
            employee = Employee.objects.filter(address=req).all()
            data = {"radio": radio_dict.get(name), "dict": employee, "employee": True}
            return render(request, 'search_extends.html', data)
        if atr == "Телефон":
            employee = Employee.objects.filter(phone=req).all()
            data = {"radio": radio_dict.get(name), "dict": employee, "employee": True}
            return render(request, 'search_extends.html', data)
        if atr == "Номер должности":
            employee = Employee.objects.filter(id_position=req).all()
            data = {"radio": radio_dict.get(name), "dict": employee, "employee": True}
            return render(request, 'search_extends.html', data)
    if name == "departments":
        if atr == "Номер":
            departments = Departments.objects.filter(id_department=req).all()
            data = {"radio": radio_dict.get(name), "dict": departments, "departments": True}
            return render(request, 'search_extends.html', data)
        if atr == "Имя":
            departments = Departments.objects.filter(name=req).all()
            data = {"radio": radio_dict.get(name), "dict": departments, "departments": True}
            return render(request, 'search_extends.html', data)
    if name == "education":
        if atr == "Номер образования":
            education = Education.objects.filter(id_education=req).all()
            data = {"radio": radio_dict.get(name), "dict": education, "education": True}
            return render(request, 'search_extends.html', data)
        if atr == "Номер сотрудника":
            education = Education.objects.filter(id_employee=req).all()
            data = {"radio": radio_dict.get(name), "dict": education, "education": True}
            return render(request, 'search_extends.html', data)
        if atr == "Тип":
            education = Education.objects.filter(type_education=req).all()
            data = {"radio": radio_dict.get(name), "dict": education, "education": True}
            return render(request, 'search_extends.html', data)
        if atr == "Имя":
            education = Education.objects.filter(name_education=req).all()
            data = {"radio": radio_dict.get(name), "dict": education, "education": True}
            return render(request, 'search_extends.html', data)
    if name == "passports":
        if atr == "id":
            passports = Pasports.objects.filter(id_pasport=req).all()
            data = {"radio": radio_dict.get(name), "dict": passports, "passports": True}
            return render(request, 'search_extends.html', data)
        if atr == "Номер сотрудника":
            passports = Pasports.objects.filter(id_employee=req).all()
            data = {"radio": radio_dict.get(name), "dict": passports, "passports": True}
            return render(request, 'search_extends.html', data)
        if atr == "Номер паспорта":
            passports = Pasports.objects.filter(number=req).all()
            data = {"radio": radio_dict.get(name), "dict": passports, "passports": True}
            return render(request, 'search_extends.html', data)
        if atr == "Кем выдан":
            passports = Pasports.objects.filter(name_give=req).all()
            data = {"radio": radio_dict.get(name), "dict": passports, "passports": True}
            return render(request, 'search_extends.html', data)
        if atr == "Дата":
            passports = Pasports.objects.filter(date=req).all()
            data = {"radio": radio_dict.get(name), "dict": passports, "passports": True}
            return render(request, 'search_extends.html', data)
    if name == "timetable":
        if atr == "Номер должности":
            timetable = Timetable.objects.filter(id_position=req).all()
            data = {"radio": radio_dict.get(name), "dict": timetable, "timetable": True}
            return render(request, 'search_extends.html', data)
        if atr == "Номер отдела":
            timetable = Timetable.objects.filter(id_department=req).all()
            data = {"radio": radio_dict.get(name), "dict": timetable, "timetable": True}
            return render(request, 'search_extends.html', data)
        if atr == "Название":
            timetable = Timetable.objects.filter(name=req).all()
            data = {"radio": radio_dict.get(name), "dict": timetable, "timetable": True}
            return render(request, 'search_extends.html', data)
        if atr == "Кол-во":
            timetable = Timetable.objects.filter(count=req).all()
            data = {"radio": radio_dict.get(name), "dict": timetable, "timetable": True}
            return render(request, 'search_extends.html', data)
    return render(request, 'search.html', {"radio": radio_dict.get(name)})


def addPageView(request, name):
    colls_dict = {
        "employee": ["Номер", "Имя", "Фамилия", "Отчество", "Пол", "Дата рождения", "Адрес", "Телефон",
                     "Номер должности"],
        "departments": ["Номер", "Имя"],
        "education": ["Номер образования", "Номер сотрудника", "Тип", "Имя"],
        "passports": ["id", "Номер сотрудника", "Номер паспорта", "Кем выдан", "Дата"],
        "timetable": ["Номер должности", "Номер отдела", "Название", "Кол-во"]
    }
    if name == "employee":
        employee = Employee()
        if request.method == "POST":
            employee.first_name = request.POST.get("first_name")
            employee.last_name = request.POST.get("last_name")
            employee.patronymic = request.POST.get("patronymic")
            employee.pol = request.POST.get("pol")
            employee.date = request.POST.get("date")
            employee.address = request.POST.get("address")
            employee.phone = request.POST.get("phone")
            employee.save()
            return HttpResponseRedirect("/")
        employee_atr = {
            "id": employee.id,
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "patronymic": employee.patronymic,
            "pol": employee.pol,
            "date": employee.date,
            "address": employee.address,
            "phone": employee.phone,
            "id_position": employee.id_position
        }
        data = {"cols": colls_dict.get(name), "select_dict": employee_atr}
        return render(request, 'edit.html', data)
    if name == "departments":
        departments = Departments()
        if request.method == "POST":
            departments.id_department = request.POST.get("id_department")
            departments.name = request.POST.get("name")
            departments.save()
            return HttpResponseRedirect("/")
        departments_atr = {
            "id_department": departments.id_department,
            "name": departments.name
        }
        data = {"cols": colls_dict.get(name), "select_dict": departments_atr}
        return render(request, 'edit.html', data)
    if name == "education":
        education = Education()
        if request.method == "POST":
            education.id_education = request.POST.get("id_education")
            education.id_employee = request.POST.get("id_employee")
            education.type_education = request.POST.get("type_education")
            education.name_education = request.POST.get("name_education")
            education.save()
            return HttpResponseRedirect("/")
        education_atr = {
            "id_education": education.id_education,
            "id_employee": education.id_employee,
            "type_education": education.type_education,
            "name_education": education.name_education
        }
        data = {"cols": colls_dict.get(name), "select_dict": education_atr}
        return render(request, 'edit.html', data)
    if name == "passports":
        passports = Pasports()
        if request.method == "POST":
            passports.id_pasport = request.POST.get("id_pasport")
            passports.id_employee = request.POST.get("id_employee")
            passports.number = request.POST.get("number")
            passports.name_give = request.POST.get("name_give")
            passports.date = request.POST.get("date")
            passports.save()
            return HttpResponseRedirect("/")
        passports_atr = {
            "id_pasport": passports.id_pasport,
            "id_employee": passports.id_employee,
            "number": passports.number,
            "name_give": passports.name_give,
            "date": passports.date
        }
        data = {"cols": colls_dict.get(name), "select_dict": passports_atr}
        return render(request, 'edit.html', data)
    if name == "timetable":
        timetable = Timetable()
        if request.method == "POST":
            timetable.id_position = request.POST.get("id_position")
            timetable.id_department = request.POST.get("id_department")
            timetable.name = request.POST.get("name")
            timetable.count = request.POST.get("count")
            timetable.save()
            return HttpResponseRedirect("/")
        timetable_atr = {
            "id_position": timetable.id_position,
            "id_department": timetable.id_department,
            "name": timetable.name,
            "count": timetable.count,
        }
        data = {"cols": colls_dict.get(name), "select_dict": timetable_atr}
        return render(request, 'edit.html', data)


def deletePageView(request, name, id):
    if name == "employee":
        employee = Employee.objects.get(id=id)
        employee.delete()
        return HttpResponseRedirect("/")
    if name == "departments":
        departments = Departments.objects.get(id_department=id)
        departments.delete()
        return HttpResponseRedirect("/")
    if name == "education":
        education = Education.objects.get(id_education=id)
        education.delete()
        return HttpResponseRedirect("/")
    if name == "passports":
        passports = Pasports.objects.get(id_pasport=id)
        passports.delete()
        return HttpResponseRedirect("/")
    if name == "timetable":
        timetable = Timetable.objects.get(id_position=id)
        timetable.delete()
        return HttpResponseRedirect("/")


def editPageView(request, name, id):
    colls_dict = {
        "employee": ["Номер", "Имя", "Фамилия", "Отчество", "Пол", "Дата рождения", "Адрес", "Телефон",
                     "Номер должности"],
        "departments": ["Номер", "Имя"],
        "education": ["Номер образования", "Номер сотрудника", "Тип", "Имя"],
        "passports": ["id", "Номер сотрудника", "Номер паспорта", "Кем выдан", "Дата"],
        "timetable": ["Номер должности", "Номер отдела", "Название", "Кол-во"]
    }
    if name == "employee":
        employee = Employee.objects.get(id=id)
        if request.method == "POST":
            employee.first_name = request.POST.get("first_name")
            employee.last_name = request.POST.get("last_name")
            employee.patronymic = request.POST.get("patronymic")
            employee.pol = request.POST.get("pol")
            employee.date = request.POST.get("date")
            employee.address = request.POST.get("address")
            employee.phone = request.POST.get("phone")
            employee.save()
            return HttpResponseRedirect("/")
        employee_atr = {
            "id": employee.id,
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "patronymic": employee.patronymic,
            "pol": employee.pol,
            "date": employee.date,
            "address": employee.address,
            "phone": employee.phone,
            "id_position": employee.id_position
        }
        data = {"cols": colls_dict.get(name), "select_dict": employee_atr}
        return render(request, 'edit.html', data)
    if name == "departments":
        departments = Departments.objects.get(id_department=id)
        if request.method == "POST":
            departments.id_department = request.POST.get("id_department")
            departments.name = request.POST.get("name")
            departments.save()
            return HttpResponseRedirect("/")
        departments_atr = {
            "id_department": departments.id_department,
            "name": departments.name
        }
        data = {"cols": colls_dict.get(name), "select_dict": departments_atr}
        return render(request, 'edit.html', data)
    if name == "education":
        education = Education.objects.get(id_education=id)
        if request.method == "POST":
            education.id_education = request.POST.get("id_education")
            education.id_employee = request.POST.get("id_employee")
            education.type_education = request.POST.get("type_education")
            education.name_education = request.POST.get("name_education")
            education.save()
            return HttpResponseRedirect("/")
        education_atr = {
            "id_education": education.id_education,
            "id_employee": education.id_employee,
            "type_education": education.type_education,
            "name_education": education.name_education
        }
        data = {"cols": colls_dict.get(name), "select_dict": education_atr}
        return render(request, 'edit.html', data)
    if name == "passports":
        passports = Pasports.objects.get(id_pasport=id)
        if request.method == "POST":
            passports.id_pasport = request.POST.get("id_pasport")
            passports.id_employee = request.POST.get("id_employee")
            passports.number = request.POST.get("number")
            passports.name_give = request.POST.get("name_give")
            passports.date = request.POST.get("date")
            passports.save()
            return HttpResponseRedirect("/")
        passports_atr = {
            "id_pasport": passports.id_pasport,
            "id_employee": passports.id_employee,
            "number": passports.number,
            "name_give": passports.name_give,
            "date": passports.date
        }
        data = {"cols": colls_dict.get(name), "select_dict": passports_atr}
        return render(request, 'edit.html', data)
    if name == "timetable":
        timetable = Timetable.objects.get(id_position=id)
        if request.method == "POST":
            timetable.id_position = request.POST.get("id_position")
            timetable.id_department = request.POST.get("id_department")
            timetable.name = request.POST.get("name")
            timetable.count = request.POST.get("count")
            timetable.save()
            return HttpResponseRedirect("/")
        timetable_atr = {
            "id_position": timetable.id_position,
            "id_department": timetable.id_department,
            "name": timetable.name,
            "count": timetable.count,
        }
        data = {"cols": colls_dict.get(name), "select_dict": timetable_atr}
        return render(request, 'edit.html', data)
