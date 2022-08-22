from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from user_panel.models import *
import xlwt
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import datetime


# Create your views here.

def admindashbord(request):
    dateon = datetime.date.today()
    mailSendReport = 0
    dailywork = TaskSheet.objects.filter(date=dateon, mailSendReport=mailSendReport)
    print(dailywork)
    return render(request, 'admindashbord.html',{'dailywork':dailywork})


def adminlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email,    

        if user is not None:
            login(request, user)
            return redirect('admindashbord')

    return render(request, 'adminlogin.html')


def adminlogout(request):
    logout(request)
    return redirect('login')


def staff_list(request):
    staff_list = Staff.objects.all().order_by('-id')
    return render(request, 'staff_list.html', {'staff_list': staff_list})


def statusChange(request, id):
    User_Staff_detail = Staff.objects.get(id=id)
    if User_Staff_detail:
        print('active')
        if User_Staff_detail.is_active:
            User_Staff_detail.is_active = False
            User_Staff_detail.save()
            return redirect('staff_list')
            # staff_list = Staff.objects.all().order_by('-id')
            # return render(request, 'staff_list.html', {'staff_list': staff_list})
        else:
            User_Staff_detail.is_active = True
            User_Staff_detail.save()
            return redirect('staff_list')
            # staff_list = Staff.objects.all().order_by('-id')
            # return render(request, 'staff_list.html', {'staff_list': staff_list})
    else:
        staff_list = Staff.objects.all().order_by('-id')
        return render(request, 'staff_list.html', {'staff_list': staff_list})


def addnewStaff(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone_no = request.POST['phone_no']
        station_id = request.POST['session_id']
        user_id = request.POST['user_id']
        machine_id = request.POST['machine_id']
        ssa_value = request.POST['ssa']
        csc = request.POST['csc']
        HODEmail = request.POST['HODEmail']
        CSCInchargeEmail = request.POST['CSCInchargeEmail']
        joining_date = request.POST['joining_date']
        end_date = request.POST['end_date']

        ssa = None
        try:
            ssa = Ssavalue.objects.get(ssa=ssa_value)
            print()
        except Ssavalue.DoesNotExist:
            ssa = Ssavalue.objects.create(ssa=ssa_value)
            ssa.save()

        city = None
        try:
            city = City.objects.get(csc=csc, ssavalue=ssa)
        except City.DoesNotExist:
            city = City.objects.create(csc=csc, ssavalue=ssa)
            city.save()

        Staff.objects.create(station_id=station_id, user_id=user_id, machine_id=machine_id, BAAdharEmail=HODEmail,
                             username=username, email=email, password=password,
                             phone_no=phone_no, CSCInchargeEmail=CSCInchargeEmail,
                             city=city, joining_date=joining_date, end_date=end_date if end_date else None)
        sendmail("Your Account authentication ", "send_mailAccount",     email,
                 {'username': username, 'email': email, 'password': password})
        return redirect('staff_list')
    else:
        messge = "Please All Filed Required"
        return render(request, 'addStaff.html')
    return render(request, 'addStaff.html')


def sendmail(subject, template, to, context, lookup_kwargs=None):
    email_user = AppData.objects.get(key="EMAIL_HOST_USER")

    template_str = template + '.html'
    html_message = render_to_string(template_str, {'data': context})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, email_user, [to], html_message=html_message)


def editStaff(request, id):
    staff_list = Staff.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        station_id = request.POST['session_id']
        ssa = request.POST['ssa']
        csc = request.POST['csc']
        user_id = request.POST['user_id']
        machine_id = request.POST['machine_id']
        BAAdharEmail = request.POST['HODEmail']
        CSCInchargeEmail = request.POST['CSCInchargeEmail']
        joining_date = request.POST['joining_date']
        end_date = request.POST['end_date']

        staff_list.username = username
        staff_list.email = email
        staff_list.phone_no = phone_no
        staff_list.station_id = station_id
        staff_list.ssa = ssa
        staff_list.csc = csc
        staff_list.user_id = user_id
        staff_list.machine_id = machine_id
        staff_list.BAAdharEmail = BAAdharEmail
        staff_list.CSCInchargeEmail = CSCInchargeEmail
        staff_list.joining_date = joining_date
        staff_list.end_date = end_date if end_date else None
        staff_list.save()
        return redirect('staff_list')
    return render(request, 'editStaff.html', {'staff_list': staff_list})


def deleteStaff(request, id):
    staff_list = Staff.objects.get(id=id).delete()
    return redirect("staff_list")


def adminstaffTaskSheet(request):
    if request.method == 'POST':
        dateOn = request.POST['from_date']
        to_date = request.POST['to_date']
        ssa = request.POST['ssa']
        staffName = request.POST['staffName']

        taskSheet = TaskSheet.objects.all().order_by('-id')
        if dateOn != '' and to_date != '':
            taskSheet = taskSheet.filter(date__range=[dateOn, to_date])
            print(taskSheet)
        if staffName != "":
            taskSheet = taskSheet.filter(username=staffName)
        if ssa != "":
            taskSheet = taskSheet.filter(ssa=ssa)
        return render(request, 'adminstaffTaskSheet.html',
                      {'taskSheet': taskSheet, 'dateOn': dateOn, 'to_date': to_date,
                       'staffName': staffName, 'ssa': ssa})
    else:
        taskSheet = TaskSheet.objects.all().order_by('-id')
        return render(request, 'adminstaffTaskSheet.html', {'taskSheet': taskSheet})


def admineditTaskSheet(request, id):
    taskSheet = TaskSheet.objects.get(id=id)
    if request.method == 'POST':
        newEnrollment = request.POST['newEnrollment']
        AadharMandatoryUpdate = request.POST['AadharMandatoryUpdate']
        AadharDemographicUpdate = request.POST['AadharDemographicUpdate']
        AadharBiometricUpdate = request.POST['AadharBiometricUpdate']
        remark = request.POST['remark']

        taskSheet.newEnrollment = newEnrollment
        taskSheet.AadharMandatoryUpdate = AadharMandatoryUpdate
        taskSheet.AadharDemographicUpdate = AadharDemographicUpdate
        taskSheet.AadharBiometricUpdate = AadharBiometricUpdate
        taskSheet.remark = remark
        taskSheet.save()
        return redirect('adminstaffTaskSheet')

    return render(request, 'admineditTaskSheet.html', {'taskSheet': taskSheet})


def admindeleteTaskSheet(request, id):
    taskSheet = TaskSheet.objects.get(id=id).delete()
    return redirect("adminstaffTaskSheet")


def taskStatusChange(request, id):
    task_StatusChange = TaskSheet.objects.get(id=id)
    if task_StatusChange:
        print(task_StatusChange.taskStatus)
        if task_StatusChange.taskStatus:
            task_StatusChange.taskStatus = False
            task_StatusChange.save()
            return redirect('adminstaffTaskSheet')
            # taskSheet = TaskSheet.objects.all().order_by('-id')
            # return render(request, 'adminstaffTaskSheet.html', {'taskSheet': taskSheet})
        else:
            task_StatusChange.taskStatus = True
            task_StatusChange.save()
            return redirect('adminstaffTaskSheet')
            # taskSheet = TaskSheet.objects.all().order_by('-id')
            # return render(request, 'adminstaffTaskSheet.html', {'taskSheet': taskSheet})
    else:
        taskSheet = TaskSheet.objects.all().order_by('-id')
        return render(request, 'adminstaffTaskSheet.html', {'taskSheet': taskSheet})


def deleteTask(request):
    id = request.POST['task_id']
    print("id..........", id)
    task = TaskSheet.objects.get(id=id)
    print(task)
    task.delete()
    return redirect('adminstaffTaskSheet')


def taskStatus(request):
    if request.method == "POST":
        task_ids = request.POST.getlist('id[]')
        btnName = request.POST['btnName']
        print(" this id ----------->", task_ids)
        print("BtnName.........", btnName)
        for id in task_ids:
            task = TaskSheet.objects.get(pk=id)
            if btnName == 'Approved':
                task.taskStatus = 0
                task.save()
            if btnName == 'Pending':
                task.taskStatus = 1
                task.save()
        return redirect('adminstaffTaskSheet')
    return redirect('adminstaffTaskSheet')


def appData_list(request):
    appdata = AppData.objects.all()
    return render(request, 'appData.html', {'appdata': appdata})


def addNewaddData(request):
    if request.method == "POST":
        key = request.POST['key']
        value = request.POST['value']

        AppData.objects.create(key=key, value=value)
        return redirect('appData_list')

    return render(request, 'addNewaddData.html')


def editappData(request, id):
    appdata = AppData.objects.get(id=id)
    if request.method == "POST":
        key = request.POST['key']
        value = request.POST['value']
        appdata.key = key
        appdata.value = value
        appdata.save()
        return redirect('appData_list')

    return render(request, 'editappData.html', {'appdata': appdata})


def export_users_xlsTaskSheet(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="taskSheet.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('TaskSheet')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'date', 'task', 'collect_amount', 'numbersOfCase', 'status', 'remark', 'taskStatus', 'staffName']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = TaskSheet.objects.all().values_list('id', 'date', 'task', 'collect_amount', 'numbersOfCase', 'status',
                                               'remark', 'taskStatus', 'staffName')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            print(row)

    wb.save(response)
    return response


def adminDailyBsnlWork(request):
    if request.method == 'POST':
        dateOn = request.POST['from_date']
        to_date = request.POST['to_date']
        ssa = request.POST['ssa']
        staffName = request.POST['staffName']
        print(dateOn, to_date, staffName)

        dailyBsnlWork = DailyBsnlWork.objects.all().order_by('-id')
        if dateOn != '' and to_date != '':
            dailyBsnlWork = dailyBsnlWork.filter(date__range=[dateOn, to_date])
            print(dailyBsnlWork)
        if staffName != "":
            dailyBsnlWork = dailyBsnlWork.filter(username=staffName)
        if ssa != "":
            dailyBsnlWork = dailyBsnlWork.filter(ssa=ssa)
        return render(request, 'adminDailyBsnlWork.html',
                      {'dailyBsnlWork': dailyBsnlWork, 'dateOn': dateOn, 'to_date': to_date,
                       'staffName': staffName, 'ssa': ssa})
    else:
        dailyBsnlWork = DailyBsnlWork.objects.all().order_by('-id')
        return render(request, 'adminDailyBsnlWork.html', {'dailyBsnlWork': dailyBsnlWork})


def admineditDailyBsnlWork(request, id):
    dailyBsnlWork = DailyBsnlWork.objects.get(id=id)
    if request.method == 'POST':
        CBPsales = request.POST['CBPsales']
        C_TopRechageSales = request.POST['C_TopRechageSales']
        C_TopFrcSales = request.POST['C_TopFrcSales']
        NormalSimSale = request.POST['NormalSimSale']
        MnpSimSale = request.POST['MnpSimSale']
        SwappingSimSale = request.POST['SwappingSimSale']
        PostpaidSimSale = request.POST['PostpaidSimSale']

        dailyBsnlWork.CBPsales = CBPsales
        dailyBsnlWork.C_TopRechageSales = C_TopRechageSales
        dailyBsnlWork.C_TopFrcSales = C_TopFrcSales
        dailyBsnlWork.NormalSimSale = NormalSimSale
        dailyBsnlWork.MnpSimSale = MnpSimSale
        dailyBsnlWork.SwappingSimSale = SwappingSimSale
        dailyBsnlWork.PostpaidSimSale = PostpaidSimSale
        dailyBsnlWork.save()
        return redirect('adminDailyBsnlWork')
    else:
        return render(request, 'admineditDailyBsnlWork.html', {'dailyBsnlWork': dailyBsnlWork})


def admindeleteDailyBsnlWork(request, id):
    dailyBsnlWork = DailyBsnlWork.objects.get(id=id).delete()
    return redirect("adminDailyBsnlWork")


def admindailyCashReport(request):
    if request.method == 'POST':
        dateOn = request.POST['from_date']
        to_date = request.POST['to_date']
        ssa = request.POST['ssa']
        staffName = request.POST['staffName']
        print(dateOn, to_date, staffName)

        dailyCashWork = DailyCashReport.objects.all().order_by('-id')
        if dateOn != '' and to_date != '':
            dailyCashWork = dailyCashWork.filter(date__range=[dateOn, to_date])
            print(dailyCashWork)
        if staffName != "":
            dailyCashWork = dailyCashWork.filter(username=staffName)
        if ssa != "":
            dailyCashWork = dailyCashWork.filter(ssa=ssa)
        return render(request, 'admindailyCashReport.html',
                      {'dailyCashWork': dailyCashWork, 'dateOn': dateOn, 'to_date': to_date,
                       'staffName': staffName, 'ssa': ssa})
    else:
        dailyCashWork = DailyCashReport.objects.all().order_by('-id')
        return render(request, 'admindailyCashReport.html', {'dailyCashWork': dailyCashWork})


def adminbalance(request):
    balance = Balance.objects.all()
    return render(request, 'adminBalance.html', {'balance': balance})


def admindeposite(request):
    deposite = DepositeCash.objects.all().order_by('-id')
    return render(request, 'admindeposite.html', {'deposite': deposite})


def adminchequeDetails(request):
    chequeDetails = ChequeDetail.objects.all().order_by('-id')
    return render(request, 'adminchequeDetails.html', {'chequeDetails': chequeDetails})


def admineditChequeDeatils(request, id):
    chequeDetails = ChequeDetail.objects.get(id=id)
    if request.method == 'POST':
        chequeNo = request.POST['chequeNo']
        chaqueDate = request.POST['chaqueDate']
        lan_phoNo = request.POST['lan_phoNo']
        amount = request.POST['amount']
        challanNumber = request.POST['challanNumber']
        personCollectingCheque = request.POST['personCollectingCheque']

        chequeDetails.chequeNo = chequeNo
        chequeDetails.chaqueDate = chaqueDate
        chequeDetails.lan_phoNo = lan_phoNo
        chequeDetails.amount = amount
        chequeDetails.challanNumber = challanNumber
        chequeDetails.personCollectingCheque = personCollectingCheque
        chequeDetails.save()

        return redirect('adminchequeDetails')
    return render(request, 'admineditChequeDeatils.html', {'chequeDetails': chequeDetails})


def admindeleteChequeDetails(request, id):
    chequeDetails = ChequeDetail.objects.get(id=id).delete()
    return redirect("adminchequeDetails")


def aadharPortalCashReport(request):
    if request.method == 'POST':
        dateOn = request.POST['from_date']
        to_date = request.POST['to_date']
        ssa = request.POST['ssa']
        staffName = request.POST['staffName']

        aadharPortalCashReport = AadharPortalCashReport.objects.all().order_by('-id')
        if dateOn != '' and to_date != '':
            aadharPortalCashReport = aadharPortalCashReport.filter(date__range=[dateOn, to_date])
            print(aadharPortalCashReport)
        if staffName != "":
            aadharPortalCashReport = aadharPortalCashReport.filter(username=staffName)
        if ssa != "":
            aadharPortalCashReport = aadharPortalCashReport.filter(ssa=ssa)
        return render(request, 'aadharPortalCashReport.html',
                      {'aadharPortalCashReport': aadharPortalCashReport, 'dateOn': dateOn, 'to_date': to_date,
                       'staffName': staffName, 'ssa': ssa})
    else:
        aadharPortalCashReport = AadharPortalCashReport.objects.all().order_by('-id')
        return render(request, 'aadharPortalCashReport.html', {'aadharPortalCashReport': aadharPortalCashReport})


def stock(request):
    stockDetails = Stock.objects.all().order_by('-id')
    return render(request, 'stock.html', {'stockDetails': stockDetails})


def adminStockUpdate(request):
    stockUpdate = StockUpdate.objects.all().order_by('-id')
    return render(request, 'adminStockUpdate.html', {'stockUpdate': stockUpdate})


def addStock(request):
    city = City.objects.all()
    ssa = Ssavalue.objects.all()
    if request.method == 'POST':
        date = request.POST['date']
        ssa = request.POST['ssa']
        city = request.POST['csc']
        CBPValue = request.POST['CBPValue']
        station_id = request.POST['station_id']
        C_TopValue = request.POST['C_TopValue']
        NormalSimSale = request.POST['NormalSimSale']
        MnpSim = request.POST['MnpSim']
        Swapping = request.POST['Swapping']
        PostpaidSim = request.POST['PostpaidSim']
        print("==========", city)

        Stock.objects.create(date=date, ssa=Ssavalue.objects.get(pk=ssa), city=City.objects.get(pk=city),
                             station_id=station_id, CBPValue=CBPValue,
                             C_TopValue=C_TopValue,
                             NormalSimSale=NormalSimSale, MnpSim=MnpSim, Swapping=Swapping, PostpaidSim=PostpaidSim)

        stockedit = StockUpdate.objects.filter(station_id=station_id)
        print(stockedit)

        if stockedit:
            stockUpdateDetails(station_id, float(CBPValue), float(C_TopValue), float(NormalSimSale), int(MnpSim),
                               int(Swapping), int(PostpaidSim))
        else:
            StockUpdate.objects.create(date=date, ssa=Ssavalue.objects.get(pk=ssa), city=City.objects.get(pk=city),
                                       station_id=station_id, CBPValue=CBPValue,
                                       C_TopValue=C_TopValue,
                                       NormalSimSale=NormalSimSale, MnpSim=MnpSim, Swapping=Swapping,
                                       PostpaidSim=PostpaidSim)
            print('added')
        return redirect('adminStockUpdate')

    return render(request, 'addStock.html', {'city': city, 'ssa': ssa})


def stockUpdateDetails(station_id, CBPValue, C_TopValue, NormalSimSale, MnpSim, Swapping, PostpaidSim):
    stockObje = StockUpdate.objects.get(station_id=station_id)

    stockObje.CBPValue = CBPValue + stockObje.CBPValue
    stockObje.C_TopValue = C_TopValue + stockObje.C_TopValue
    stockObje.NormalSimSale = NormalSimSale + stockObje.NormalSimSale
    stockObje.MnpSim = MnpSim + stockObje.MnpSim
    stockObje.Swapping = Swapping + stockObje.Swapping
    stockObje.PostpaidSim = PostpaidSim + stockObje.PostpaidSim
    stockObje.save()


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


class GetCSCApiView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, pk):
        csc = City.objects.filter(ssavalue=pk)
        dict = {}
        for i in csc:
            dict[i.pk] = i.csc
        return Response(dict)


class GetStationIdView(APIView):

    def get(self, request, pk):
        station_id = Staff.objects.filter(city=pk)
        dict = {}
        for i in station_id:
            dict[i.pk] = i.station_id
        return Response(dict)
