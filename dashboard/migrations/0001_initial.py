from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=30)),
                ('clientAddress', models.CharField(max_length=50)),
                ('clientGstin', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=20)),
                ('monthlyBasic', models.FloatField(default=0.0)),
                ('monthlyHRA', models.FloatField(default=0.0)),
                ('monthlyAllowance', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('employeeName', models.CharField(max_length=25)),
                ('aadhar', models.CharField(max_length=12)),
                ('mobileNum', models.CharField(max_length=10)),
                ('account', models.CharField(max_length=50)),
                ('accountIFSC', models.CharField(max_length=50)),
                ('accountName', models.CharField(max_length=50)),
                ('pan', models.CharField(max_length=15, null=True)),
                ('uan', models.CharField(max_length=30, null=True)),
                ('esi', models.CharField(max_length=30, null=True)),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Designation')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteName', models.CharField(max_length=30)),
                ('clientName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='dashboard.Client')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='siteName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Site'),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.IntegerField()),
                ('claculatedBasic', models.FloatField(default=0.0, editable=False)),
                ('calculatedHRA', models.FloatField(default=0.0, editable=False)),
                ('calculatedAllowance', models.FloatField(default=0.0, editable=False)),
                ('calculatedPF', models.FloatField(default=0.0, editable=False)),
                ('calculatedESI', models.FloatField(default=0.0, editable=False)),
                ('netPay', models.FloatField(default=0.0, editable=False)),
                ('monthDays', models.IntegerField(default=1)),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Employee')),
            ],
        ),
    ]
