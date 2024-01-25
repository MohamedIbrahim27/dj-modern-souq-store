# Generated by Django 4.2 on 2024-01-25 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='all_total',
            field=models.IntegerField(default=0, verbose_name='Total'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('تم الشحن', 'تم الشحن'), ('جاري الشحن', 'جاري الشحن')], default='جاري الشحن', max_length=20),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdetails_set', to='orders.order'),
        ),
        migrations.CreateModel(
            name='Discount_Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_coupon', models.CharField(max_length=10, verbose_name='coupon')),
                ('discount_value', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Discount Coupon',
                'verbose_name_plural': 'Discount Coupons',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.discount_coupon', verbose_name='Discount Coupon'),
        ),
    ]
