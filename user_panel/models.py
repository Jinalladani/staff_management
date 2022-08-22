from django.db import models


# Create your models here.
class Staff(models.Model):
    city = models.ForeignKey("City", related_name="Station", on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    otp = models.CharField(max_length=6, default=359)
    is_active = models.BooleanField(default=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    machine_id = models.CharField(max_length=255, blank=True, null=True)
    BAAdharEmail = models.EmailField(blank=True, null=True)
    CSCInchargeEmail = models.EmailField(blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.username


class TaskSheet(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    ssa = models.CharField(max_length=255, blank=True, null=True)
    csc = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    machine_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    newEnrollment = models.IntegerField(blank=True, null=True)
    AadharMandatoryUpdate = models.IntegerField(blank=True, null=True)
    AadharDemographicUpdate = models.IntegerField(blank=True, null=True)
    AadharBiometricUpdate = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=512)
    taskStatus = models.BooleanField(default=True)
    mailSendReport = models.BooleanField(default=False)
    HTMLFile = models.FileField(upload_to='media/aadharwork/', verbose_name='file', null=True, blank=True)


class City(models.Model):
    ssavalue = models.ForeignKey("Ssavalue", on_delete=models.CASCADE, null=True, blank=True)
    csc = models.CharField(max_length=255, blank=True, null=True)


class Ssavalue(models.Model):
    ssa = models.CharField(max_length=255, blank=True, null=True)


class AppData(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return str(self.key)


class DailyBsnlWork(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    ssa = models.CharField(max_length=255, blank=True, null=True)
    csc = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    CBPsales = models.FloatField(blank=True, null=True)
    C_TopRechageSales = models.FloatField(blank=True, null=True)
    C_TopFrcSales = models.FloatField(blank=True, null=True)
    NormalSimSale = models.IntegerField(blank=True, null=True)
    MnpSimSale = models.IntegerField(blank=True, null=True)
    SwappingSimSale = models.IntegerField(blank=True, null=True)
    PostpaidSimSale = models.IntegerField(blank=True, null=True)


class DailyCashReport(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    ssa = models.CharField(max_length=255, blank=True, null=True)
    csc = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    aadharCash = models.FloatField(blank=True, null=True)
    CBPcash = models.FloatField(blank=True, null=True)
    C_TopCash = models.FloatField(blank=True, null=True)
    NormalSimCash = models.FloatField(blank=True, null=True)
    MnpSimCash = models.FloatField(blank=True, null=True)
    SwappingSimCash = models.FloatField(blank=True, null=True)
    PostpaidSimCash = models.FloatField(blank=True, null=True)
    DailyTotalCollection = models.FloatField(blank=True, null=True)
    opeingCashBalance = models.FloatField(blank=True, null=True)
    cashInHand = models.FloatField(blank=True, null=True)


class Balance(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    ssa = models.CharField(max_length=255, blank=True, null=True)
    csc = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    account = models.CharField(max_length=100)
    balance_amount = models.FloatField(max_length=500)


class DepositeCash(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    ssa = models.CharField(max_length=255, blank=True, null=True)
    csc = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    transaction_type = models.CharField(max_length=255, blank=True, null=True)
    personName = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField()
    fileStore = models.FileField(upload_to='media/depositeRecepite/', verbose_name='file', null=True, blank=True)


class ChequeDetail(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    ssa = models.CharField(max_length=255, blank=True, null=True)
    csc = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    chequeNo = models.CharField(max_length=255)
    chaqueDate = models.DateField()
    lan_phoNo = models.CharField(max_length=12, blank=True, null=True)
    amount = models.FloatField(max_length=255)
    challanNumber = models.CharField(max_length=255)
    personCollectingCheque = models.CharField(max_length=255, blank=True, null=True)


class AadharPortalCashReport(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    machine_id = models.CharField(max_length=255, blank=True, null=True)
    ssa = models.CharField(max_length=255, blank=True, null=True)
    csc = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    newEnrollment = models.FloatField(blank=True, null=True)
    AadharMandatoryUpdate = models.FloatField(blank=True, null=True)
    AadharDemographicUpdate = models.FloatField(blank=True, null=True)
    AadharBiometricUpdate = models.FloatField(blank=True, null=True)
    totalAmount = models.FloatField(blank=True, null=True)
    HTMLFile = models.FileField(upload_to='media/aadharPortalCashReoprt/', verbose_name='file', null=True, blank=True)


class Stock(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE, null=True, blank=True)
    ssa = models.ForeignKey("Ssavalue", on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    CBPValue = models.IntegerField(blank=True, null=True)
    C_TopValue = models.IntegerField(blank=True, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    NormalSimSale = models.IntegerField(blank=True, null=True)
    MnpSim = models.IntegerField(blank=True, null=True)
    Swapping = models.IntegerField(blank=True, null=True)
    PostpaidSim = models.IntegerField(blank=True, null=True)


class StockUpdate(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE, null=True, blank=True)
    ssa = models.ForeignKey("Ssavalue", on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    CBPValue = models.FloatField(blank=True, null=True)
    C_TopValue = models.FloatField(blank=True, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    NormalSimSale = models.IntegerField(blank=True, null=True)
    MnpSim = models.IntegerField(blank=True, null=True)
    Swapping = models.IntegerField(blank=True, null=True)
    PostpaidSim = models.IntegerField(blank=True, null=True)


class Otf(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    ssa = models.CharField(max_length=255, blank=True, null=True)
    csc = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    amount = models.FloatField()


class weeklyReport(models.Model):
    staff_key = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    ssa = models.CharField(max_length=255, blank=True, null=True)
    csc = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()


