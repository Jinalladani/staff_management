import csv
import datetime
from random import randint
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    if 'email' and 'station_id' in request.session:
        station_id = request.session['station_id']
        dateon = datetime.date.today()
        dailywork = TaskSheet.objects.filter(station_id=station_id, date=dateon)
        print(dailywork)
        return render(request, 'index.html', {'dailywork': dailywork})
    else:
        return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            uid = Staff.objects.get(email=email)
            print(uid)
            if uid.is_active:
                print(uid.email)
                if uid.email == email and uid.password == password:
                    print('redirect', {'user': uid})
                    request.session['username'] = uid.username
                    request.session['email'] = uid.email
                    request.session['id'] = uid.id
                    request.session['station_id'] = uid.station_id
                    request.session['user_id'] = uid.user_id
                    request.session['machine_id'] = uid.machine_id
                    request.session['city_id'] = uid.city_id
                    request.session['BAAdharEmail'] = uid.BAAdharEmail
                    request.session['CSCInchargeEmail'] = uid.CSCInchargeEmail
                    print(uid.city_id)
                    return render(request, 'index.html', {'uid': uid})
        except:
            message = 'Email Invalid'
            return render(request, 'login.html', {'message': message})
        message = 'Email And Password Invalid'
        return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def forgot_password(request):
    return render(request, 'forgot_password.html')


def send_otp(request):
    email = request.POST['email']
    generate_otp = randint(1111, 9999)
    uid = Staff.objects.filter(email=email)
    print(uid)
    if uid:
        uid.update(otp=generate_otp)
        print(generate_otp)
        sendmail(" Forgot Password ", "mail_template", email, {'otp': generate_otp, 'uid': uid})
        return render(request, 'reset_password.html', {'email': email, 'otp': generate_otp})
    else:
        message = "Email does not exist"
        return render(request, 'forgot_password.html', {'message': message})


def sendmail(subject, template, to, context, lookup_kwargs=None):
    email_user = AppData.objects.get(key="EMAIL_HOST_USER")

    template_str = template + '.html'
    html_message = render_to_string(template_str, {'data': context})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, email_user, [to], html_message=html_message)


def reset_password(request):
    try:
        email = request.POST['email']
        otp = request.POST['otp']
        otp1 = request.POST['otp1']
        password = request.POST['password']
        cpassword = request.POST['password']
        uid = Staff.objects.get(email=email)
        if uid:
            if otp1 == otp and password == cpassword:
                uid.password = password
                uid.save()
                message = "password reset succesfully"
                print(message)
                return redirect('login')
            else:
                message = "invalid otp or password"
                print(message)
                return render(request, 'reset_password.html', {'message': message})
    except:
        message = "invalid Email"
        print(message)
        return render(request, 'login.html', {'message': message})


def demo(request):
    return render(request, 'demo.html')


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def staffTask(request):
    if 'email' and 'username' in request.session:
        print(request.session['email'])
        staff_key = request.session['id']
        station_id = request.session['station_id']
        user_id = request.session['user_id']
        machine_id = request.session['machine_id']
        username = request.session['username']
        city_id = request.session['city_id']
        city = City.objects.get(id=city_id)
        csc = city.csc
        ssaVal = city.ssavalue_id
        ssaValue = Ssavalue.objects.get(id=ssaVal)
        ssa = ssaValue.ssa
        if request.method == 'POST':
            date = request.POST['date']
            newEnrollment = request.POST['newEnrollment']
            AadharMandatoryUpdate = request.POST['AadharMandatoryUpdate']
            AadharDemographicUpdate = request.POST['AadharDemographicUpdate']
            AadharBiometricUpdate = request.POST['AadharBiometricUpdate']
            remark = request.POST['remark']
            htmlfile = request.FILES['htmlfile']
            staff_obj = Staff.objects.get(pk=staff_key)
            created_tasksheet = TaskSheet.objects.create(date=date, newEnrollment=newEnrollment,
                                                         AadharMandatoryUpdate=AadharMandatoryUpdate,
                                                         AadharDemographicUpdate=AadharDemographicUpdate,
                                                         AadharBiometricUpdate=AadharBiometricUpdate,
                                                         HTMLFile=htmlfile,
                                                         username=username, remark=remark, station_id=station_id,
                                                         machine_id=machine_id, user_id=user_id,
                                                         csc=csc, ssa=ssa, staff_key=staff_obj)

            totalnewEnrollment = 0 * float(newEnrollment)
            totalAadharMandatoryUpdate = 0 * float(AadharMandatoryUpdate)
            totalAadharDemographicUpdate = 50 * float(AadharDemographicUpdate)
            totalAadharBiometricUpdate = 100 * float(AadharBiometricUpdate)
            totalamount = totalnewEnrollment + totalAadharMandatoryUpdate + totalAadharDemographicUpdate + totalAadharBiometricUpdate

            AadharPortalCashReport.objects.create(date=date, newEnrollment=totalnewEnrollment,
                                                  AadharMandatoryUpdate=totalAadharMandatoryUpdate,
                                                  AadharDemographicUpdate=totalAadharDemographicUpdate,
                                                  AadharBiometricUpdate=totalAadharBiometricUpdate,
                                                  totalAmount=totalamount,
                                                  HTMLFile=htmlfile,
                                                  username=username, station_id=station_id,
                                                  machine_id=machine_id, user_id=user_id,
                                                  csc=csc, ssa=ssa, staff_key=staff_obj)

            return redirect('taskSheet')

        return render(request, 'staffTask.html')
    else:
        return render(request, 'login.html')


def taskSheet(request):
    if 'email' in request.session:
        staff_key = request.session['id']
        taskSheet = TaskSheet.objects.filter(staff_key=Staff.objects.get(pk=staff_key)).order_by('-id')
        return render(request, 'taskSheet.html', {'taskSheet': taskSheet})
    else:
        return render(request, 'login.html')


def editTaskSheet(request, id):
    if 'email' in request.session:
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
            return redirect('taskSheet')

        return render(request, 'editTaskSheet.html', {'taskSheet': taskSheet})
    else:
        return render(request, 'login.html')


def deleteStaffTask(request, id):
    taskSheet = TaskSheet.objects.get(id=id).delete()
    return redirect("taskSheet")


def dailyBsnlWork(request):
    if 'email' in request.session:
        staff_key = request.session['id']
        # dailyFile = DailyFileAttach.objects.filter(staff_key=Staff.objects.get(pk=staff_key)).order_by('-id')
        dailyBsnlWork = DailyBsnlWork.objects.filter(staff_key=Staff.objects.get(pk=staff_key)).order_by('-id')
        return render(request, 'dailyBsnlWork.html', {'dailyBsnlWork': dailyBsnlWork})
    else:
        return render(request, 'login.html')


def addnewDailyBsnlWork(request):
    if 'email' and 'username' in request.session:
        print(request.session['email'])
        staff_key = request.session['id']
        station_id = request.session['station_id']
        username = request.session['username']
        city_id = request.session['city_id']
        city = City.objects.get(id=city_id)
        csc = city.csc
        ssaVal = city.ssavalue_id
        ssaValue = Ssavalue.objects.get(id=ssaVal)
        ssa = ssaValue.ssa
        if request.method == 'POST':
            date = request.POST['date']
            CBPsales = request.POST['CBPsales']
            C_TopRechageSales = request.POST['C_TopRechageSales']
            C_TopFrcSales = request.POST['C_TopFrcSales']
            NormalSimSale = request.POST['NormalSimSale']
            MnpSimSale = request.POST['MnpSimSale']
            SwappingSimSale = request.POST['SwappingSimSale']
            PostpaidSimSale = request.POST['PostpaidSimSale']
            staff_obj = Staff.objects.get(pk=staff_key)

            stockedit = StockUpdate.objects.filter(station_id=station_id)
            print(stockedit)
            if stockedit:
                cValue = float(C_TopRechageSales) + float(C_TopFrcSales)
                print(cValue)
                stockUpdateBsnl(station_id, float(CBPsales), float(cValue), float(NormalSimSale),
                                float(MnpSimSale),
                                float(SwappingSimSale), float(PostpaidSimSale))
                DailyBsnlWork.objects.create(date=date, CBPsales=CBPsales, C_TopRechageSales=C_TopRechageSales,
                                             C_TopFrcSales=C_TopFrcSales,
                                             NormalSimSale=NormalSimSale, MnpSimSale=MnpSimSale,
                                             SwappingSimSale=SwappingSimSale,
                                             PostpaidSimSale=PostpaidSimSale, username=username, station_id=station_id,
                                             ssa=ssa, csc=csc, staff_key=staff_obj)
                return redirect('dailyBsnlWork')
            else:
                return render(request, 'addnewDailyBsnlWork.html')
        else:
            return render(request, 'addnewDailyBsnlWork.html')
    else:
        return render(request, 'login.html')


def stockUpdateBsnl(station_id, CBPValue, C_TopValue, NormalSimSale, MnpSim, Swapping, PostpaidSim):
    stockObje = StockUpdate.objects.get(station_id=station_id)

    stockObje.CBPValue = stockObje.CBPValue - CBPValue
    stockObje.C_TopValue = stockObje.C_TopValue - C_TopValue
    stockObje.NormalSimSale = stockObje.NormalSimSale - NormalSimSale
    stockObje.MnpSim = stockObje.MnpSim - MnpSim
    stockObje.Swapping = stockObje.Swapping - Swapping
    stockObje.PostpaidSim = stockObje.PostpaidSim - PostpaidSim
    stockObje.save()


def editDailyBsnlWork(request, id):
    if 'email' in request.session:
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
            return redirect('dailyBsnlWork')
        else:
            return render(request, 'editDailyBsnlWork.html', {'dailyBsnlWork': dailyBsnlWork})
    else:
        return render(request, 'login.html')


def deleteDailyBsnlWork(request, id):
    dailyBsnlWork = DailyBsnlWork.objects.get(id=id).delete()
    return redirect("dailyBsnlWork")


def dailyCashReport(request):
    staff_key = request.session['id']
    dailyCashWork = DailyCashReport.objects.filter(staff_key=Staff.objects.get(pk=staff_key)).order_by('-id')
    return render(request, 'dailyCashReport.html', {'dailyCashWork': dailyCashWork})


def addDailyCashReport(request):
    if 'email' and 'username' in request.session:
        print(request.session['email'])
        staff_key = request.session['id']
        station_id = request.session['station_id']
        username = request.session['username']
        city_id = request.session['city_id']
        city = City.objects.get(id=city_id)
        csc = city.csc
        ssaVal = city.ssavalue_id
        ssaValue = Ssavalue.objects.get(id=ssaVal)
        ssa = ssaValue.ssa
        if request.method == 'POST':
            date = request.POST['date']
            aadharCash = request.POST['aadharCash']
            CBPcash = request.POST['CBPcash']
            C_TopCash = request.POST['C_TopCash']
            NormalSimCash = request.POST['NormalSimCash']
            MnpSimCash = request.POST['MnpSimCash']
            SwappingSimCash = request.POST['SwappingSimCash']
            PostpaidSimCash = request.POST['PostpaidSimCash']
            staff_obj = Staff.objects.get(pk=staff_key)

            DailyTotalCollection = float(aadharCash) + float(CBPcash) + float(C_TopCash) + float(NormalSimCash) + float(
                MnpSimCash) + float(SwappingSimCash) + float(PostpaidSimCash)
            print(DailyTotalCollection)
            opeingCashBalance = 0
            balance_set = Balance.objects.filter(staff_key=Staff.objects.get(pk=staff_key))
            print("balance ------------>", balance_set)
            for balance in balance_set:
                opeingCashBalance = float(balance.balance_amount)
            print(opeingCashBalance)

            cashInHand = float(opeingCashBalance) + float(DailyTotalCollection)
            print(cashInHand)

            DailyCashReport.objects.create(date=date, username=username, station_id=station_id,
                                           ssa=ssa, csc=csc, aadharCash=aadharCash, CBPcash=CBPcash,
                                           C_TopCash=C_TopCash, NormalSimCash=NormalSimCash, MnpSimCash=MnpSimCash,
                                           SwappingSimCash=SwappingSimCash, PostpaidSimCash=PostpaidSimCash,
                                           DailyTotalCollection=DailyTotalCollection,
                                           opeingCashBalance=opeingCashBalance,
                                           cashInHand=cashInHand, staff_key=staff_obj)
            updateBalanceValue(cashInHand, request)
            return redirect('dailyCashReport')
        else:
            return render(request, 'addDailyCashReport.html')
    else:
        return render(request, 'login.html')


def updateBalanceValue(cashInHand, request):
    if 'email' in request.session:
        staff_key = request.session['id']
        caseObject = Balance.objects.get(staff_key=Staff.objects.get(pk=staff_key))
        print("cbc -------------", cashInHand)
        print(caseObject)
        caseObject.balance_amount = cashInHand
        caseObject.save()
    else:
        return render(request, 'login.html')


def balance(request):
    if 'email' in request.session:
        staff_key = request.session['id']
        balance = Balance.objects.filter(staff_key=Staff.objects.get(pk=staff_key))
        return render(request, 'Balance.html', {'balance': balance})
    else:
        return render(request, 'login.html')


def addBalance(request):
    if 'email' and 'username' in request.session:
        print(request.session['email'])
        staff_key = request.session['id']
        station_id = request.session['station_id']
        username = request.session['username']
        city_id = request.session['city_id']
        city = City.objects.get(id=city_id)
        csc = city.csc
        ssaVal = city.ssavalue_id
        ssaValue = Ssavalue.objects.get(id=ssaVal)
        ssa = ssaValue.ssa
        if request.method == 'POST':
            type = request.POST['type']
            balnce_amount = request.POST['balnce_amount']
            staff_obj = Staff.objects.get(pk=staff_key)
            data = Balance.objects.filter(staff_key=staff_obj, account='Cash')
            if data:
                print("already there")
            else:
                Balance.objects.create(username=username, station_id=station_id,
                                       ssa=ssa, csc=csc, account=type, balance_amount=balnce_amount,
                                       staff_key=staff_obj)
            return redirect('balance')

        else:
            return render(request, 'addBalance.html')
    else:
        return render(request, 'login.html')


def deposite(request):
    if 'email' in request.session:
        staff_key = request.session['id']
        deposite = DepositeCash.objects.filter(staff_key=Staff.objects.get(pk=staff_key)).order_by('-id')
        return render(request, 'deposite.html', {'deposite': deposite})
    else:
        return render(request, 'login.html')


def addDeposite(request):
    if 'email' and 'username' in request.session:
        print(request.session['email'])
        staff_key = request.session['id']
        station_id = request.session['station_id']
        username = request.session['username']
        city_id = request.session['city_id']
        city = City.objects.get(id=city_id)
        csc = city.csc
        ssaVal = city.ssavalue_id
        ssaValue = Ssavalue.objects.get(id=ssaVal)
        ssa = ssaValue.ssa
        if request.method == 'POST':
            date = request.POST['date']
            transaction_type = request.POST['transaction_type']
            person_name = request.POST['person_name']
            amount = request.POST['amount']
            fileStore = request.FILES['fileStore']
            staff_obj = Staff.objects.get(pk=staff_key)

            balance_set = Balance.objects.filter(staff_key=Staff.objects.get(pk=staff_key))
            print("balance ------------>", balance_set)
            for balance in balance_set:
                opeingCashBalance = float(balance.balance_amount)
            print(opeingCashBalance)

            deposie_amount = float(opeingCashBalance) - float(amount)
            print(deposie_amount)

            DepositeCash.objects.create(username=username, station_id=station_id,
                                        ssa=ssa, csc=csc, date=date, amount=amount, transaction_type=transaction_type,
                                        personName=person_name, fileStore=fileStore,
                                        staff_key=staff_obj)

            updateBalanceValue(deposie_amount, request)
            return redirect('deposite')
        else:
            return render(request, 'addDeposite.html')
    else:
        return render(request, 'login.html')


def chequeDetails(request):
    if 'email' in request.session:
        staff_key = request.session['id']
        chequeDetails = ChequeDetail.objects.filter(staff_key=Staff.objects.get(pk=staff_key)).order_by('-id')
        return render(request, 'chequeDetails.html', {'chequeDetails': chequeDetails})
    else:
        return render(request, 'login.html')


def addChequeDetails(request):
    if 'email' and 'username' in request.session:
        print(request.session['email'])
        staff_key = request.session['id']
        station_id = request.session['station_id']
        username = request.session['username']
        city_id = request.session['city_id']
        city = City.objects.get(id=city_id)
        csc = city.csc
        ssaVal = city.ssavalue_id
        ssaValue = Ssavalue.objects.get(id=ssaVal)
        ssa = ssaValue.ssa
        if request.method == 'POST':
            date = request.POST['date']
            chequeNo = request.POST['chequeNo']
            chaqueDate = request.POST['chaqueDate']
            lan_phoNo = request.POST['lan_phoNo']
            amount = request.POST['amount']
            challanNumber = request.POST['challanNumber']
            personCollectingCheque = request.POST['personCollectingCheque']
            staff_obj = Staff.objects.get(pk=staff_key)

            ChequeDetail.objects.create(date=date, username=username, station_id=station_id,
                                        ssa=ssa, csc=csc, chequeNo=chequeNo, chaqueDate=chaqueDate,
                                        lan_phoNo=lan_phoNo, amount=amount, challanNumber=challanNumber,
                                        personCollectingCheque=personCollectingCheque,
                                        staff_key=staff_obj)
            return redirect('chequeDetails')

        else:
            return render(request, 'addChequeDetails.html')
    else:
        return render(request, 'login.html')


def editChequeDeatils(request, id):
    if 'email' in request.session:
        chequeDetails = ChequeDetail.objects.get(id=id)
        print(chequeDetails)
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

            return redirect('chequeDetails')
        else:
            return render(request, 'editChequeDeatils.html', {'chequeDetails': chequeDetails})
    else:
        return render(request, 'login.html')


def deleteChequeDetails(request, id):
    chequeDetails = ChequeDetail.objects.get(id=id).delete()
    return redirect("chequeDetails")


def stockDetails(request):
    if 'email' and 'username' and 'station_id' in request.session:
        station_id = request.session['station_id']
        print(station_id)
        stockdet = StockUpdate.objects.filter(station_id=station_id).order_by('id')
        print(stockdet)
        return render(request, 'stockDetails.html', {'stockdet': stockdet})
    else:
        return render(request, 'login.html')


def otfValue(request):
    if 'email' in request.session:
        staff_key = request.session['id']
        otf = Otf.objects.filter(staff_key=Staff.objects.get(pk=staff_key)).order_by('-id')
        return render(request, 'otf.html', {'otf': otf})
    else:
        return render(request, 'login.html')


def addOtf(request):
    if 'email' and 'username' in request.session:
        print(request.session['email'])
        staff_key = request.session['id']
        station_id = request.session['station_id']
        username = request.session['username']
        city_id = request.session['city_id']
        city = City.objects.get(id=city_id)
        csc = city.csc
        ssaVal = city.ssavalue_id
        ssaValue = Ssavalue.objects.get(id=ssaVal)
        ssa = ssaValue.ssa
        if request.method == 'POST':
            date = request.POST['date']
            amount = request.POST['amount']
            staff_obj = Staff.objects.get(pk=staff_key)

            stockedit = StockUpdate.objects.filter(station_id=station_id)
            print(stockedit)

            if stockedit:
                Otf.objects.create(date=date, amount=amount, username=username, station_id=station_id,
                                   ssa=ssa, csc=csc, staff_key=staff_obj)

                updateOtfValue(float(amount), request)

                return redirect('otfValue')

        return render(request, 'addOtf.html')
    else:
        return render(request, 'login.html')


def updateOtfValue(amount, request):
    if 'email' and 'station_id' in request.session:
        staff_key = request.session['station_id']
        caseObject = StockUpdate.objects.get(station_id=staff_key)
        print("cbc -------------", amount)
        print(caseObject.C_TopValue)
        caseObject.C_TopValue = caseObject.C_TopValue + float(amount)
        caseObject.save()
    else:
        return render(request, 'login.html')


def weeklyReport(request):
    if 'email' in request.session:
        return render(request, 'weeklyReport.html')
    else:
        return render(request, 'login.html')


def sendDailyMail(request):
    if 'email' and 'station_id' and 'CSCInchargeEmail' and 'BAAdharEmail' in request.session:
        dateon = datetime.date.today()
        station_id = request.session['station_id']
        CSCInchargeEmail = request.session['CSCInchargeEmail']
        BAAdharEmail = request.session['BAAdharEmail']
        dailytask = TaskSheet.objects.filter(date=dateon, station_id=station_id)
        print(dailytask)
        dailyBSNLtask = DailyBsnlWork.objects.filter(date=dateon, station_id=station_id)
        print(dailyBSNLtask)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Dailywork' + str(datetime.datetime.now()) + '.csv'

        for HTML in dailytask:
            daily = HTML.HTMLFile
        print(daily)
        daily.url

        # responseHTML = HttpResponse(content_type='text/csv')
        # responseHTML['Content-Disposition'] = daily.url
        # print('---------------------------------',responseHTML)

        writer = csv.writer(response)
        writer.writerow(
            ['date', 'station_id', 'ssa', 'csc', 'username', 'machine_id',
             'user_id', 'newEnrollment', 'AadharMandatoryUpdate', 'AadharDemographicUpdate',
             'AadharBiometricUpdate'])

        valuestore = dailytask

        for exp in valuestore:
            writer.writerow([exp.date, exp.station_id, exp.ssa, exp.csc, exp.username,
                             exp.machine_id,
                             exp.user_id, exp.newEnrollment, exp.AadharMandatoryUpdate,
                             exp.AadharDemographicUpdate,
                             exp.AadharBiometricUpdate])

        writer = csv.writer(response)
        writer.writerow(
            ['date', 'station_id', 'ssa', 'csc', 'username', 'CBPsales',
             'C_TopRechageSales', 'NormalSimSale', 'MnpSimSale', 'SwappingSimSale',
             'PostpaidSimSale'])

        valuestore = dailyBSNLtask

        for exp in valuestore:
            writer.writerow([exp.date, exp.station_id, exp.ssa, exp.csc, exp.username,
                             exp.CBPsales,
                             exp.C_TopRechageSales, exp.NormalSimSale, exp.MnpSimSale,
                             exp.SwappingSimSale,
                             exp.PostpaidSimSale])

        EMAIL_USER = 'vishalseth066@gmail.com'

        email = EmailMessage('Daily Work', 'Aadhar Work & BSNL Work', EMAIL_USER,
                             [BAAdharEmail, CSCInchargeEmail])
        email.attach('attachment_file_name.csv', response.getvalue(), 'text/csv')
        email.attach('attachment_file_name.csv', daily.getvalue(), 'text/csv')
        email.send(fail_silently=False)

        for e in dailytask:
            e.mailSendReport = True
            e.save()

        return redirect('index')
    else:
        return render(request, 'login.html')
