# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-05 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='file/')),
                ('email', models.EmailField(default='', max_length=254)),
                ('country', models.CharField(choices=[('Andorra', 'Andorra'), ('United Arab Emirates', 'United Arab Emirates'), ('Afghanistan', 'Afghanistan'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Albania', 'Albania'), ('Armenia', 'Armenia'), ('Netherlands', 'Netherlands Antilles'), ('Angola', 'Angola'), ('Antarctica', 'Antarctica'), ('Argentina', 'Argentina'), ('American', 'American Samoa'), ('Austria', 'Austria'), ('Australia', 'Australia'), ('Aruba', 'Aruba'), ('Azerbaijan', 'Azerbaijan'), ('Bosnia', 'Bosnia and Herzegovina'), ('Barbados', 'Barbados'), ('Bangladesh', 'Bangladesh'), ('Belgium', 'Belgium'), ('Burkina', 'Burkina Faso'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Burundi', 'Burundi'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Brunei', 'Brunei Darussalam'), ('Bolivia', 'Bolivia'), ('Brazil', 'Brazil'), ('Bahama', 'Bahama'), ('Bhutan', 'Bhutan'), ('Bouvet', 'Bouvet Island'), ('Botswana', 'Botswana'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Canada', 'Canada'), ('Cocos', 'Cocos (Keeling) Islands'), ('Central', 'Central African Republic'), ('Congo', 'Congo'), ('Switzerland', 'Switzerland'), ('Ivory', 'Ivory Coast'), ('Cook Iislands', 'Cook Iislands'), ('Chile', 'Chile'), ('Cameroon', 'Cameroon'), ('China', 'China'), ('Colombia', 'Colombia'), ('Costa Rica', 'Costa Rica'), ('Cuba', 'Cuba'), ('Cape Verde', 'Cape Verde'), ('Christmas', 'Christmas Island'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Germany', 'Germany'), ('Djibouti', 'Djibouti'), ('Denmark', 'Denmark'), ('Dominica', 'Dominica'), ('Dominican', 'Dominican Republic'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Estonia', 'Estonia'), ('Egypt', 'Egypt'), ('Western Sahara', 'Western Sahara'), ('Eritrea', 'Eritrea'), ('Spain', 'Spain'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland', 'Falkland Islands (Malvinas)'), ('Micronesia', 'Micronesia'), ('Faroe Islands', 'Faroe Islands'), ('France', 'France'), ('France, Metropolitan', 'France, Metropolitan'), ('Gabon', 'Gabon'), ('United Kingdom (Great Britain)', 'United Kingdom (Great Britain)'), ('Grenada', 'Grenada'), ('Georgia', 'Georgia'), ('French', 'French Guiana'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greenland', 'Greenland'), ('Gambia', 'Gambia'), ('Guinea', 'Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Equatorial', 'Equatorial Guinea'), ('Greece', 'Greece'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('Guatemala', 'Guatemala'), ('Guam', 'Guam'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Hong Kong', 'Hong Kong'), ('Heard & McDonald Islands', 'Heard & McDonald Islands'), ('Honduras', 'Honduras'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Indonesia', 'Indonesia'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('India', 'India'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Iraq', 'Iraq'), ('Islamic Republic of Iran', 'Islamic Republic of Iran'), ('Iceland', 'Iceland'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Jordan', 'Jordan'), ('Japan', 'Japan'), ('Kenya', 'Kenya'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Cambodia', 'Cambodia'), ('Kiribati', 'Kiribati'), ('Comoros', 'Comoros'), ('St. Kitts and Nevis', 'St. Kitts and Nevis'), ('Korea', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('Kuwait', 'Kuwait'), ('Cayman Islands', 'Cayman Islands'), ('Kazakhstan', 'Kazakhstan'), ('Lao People', "Lao People's Democratic Republic"), ('Lebanon', 'Lebanon'), ('Saint Lucia', 'Saint Lucia'), ('Liechtenstein', 'Liechtenstein'), ('Sri Lanka', 'Sri Lanka'), ('Liberia', 'Liberia'), ('Lesotho', 'Lesotho'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Latvia', 'Latvia'), ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Moldova, Republic of', 'Moldova, Republic of'), ('Madagascar', 'Madagascar'), ('Marshall Island', 'Marshall Islands'), ('Mali', 'Mali'), ('Mongolia', 'Mongolia'), ('Myanmar', 'Myanmar'), ('Macau', 'Macau'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('MS', 'Monserrat'), ('Malta', 'Malta'), ('Mauritius', 'Mauritius'), ('Maldives', 'Maldives'), ('Malawi', 'Malawi'), ('Mexico', 'Mexico'), ('Malaysia', 'Malaysia'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('Niue', 'Niue'), ('Zealand', 'New Zealand'), ('Oman', 'Oman'), ('Panama', 'Panama'), ('Peru', 'Peru'), ('French Polynesia', 'French Polynesia'), ('Papua New Guinea', 'Papua New Guinea'), ('Philippines', 'Philippines'), ('Pakistan', 'Pakistan'), ('Poland', 'Poland'), ('St. Pierre & Miquelon', 'St. Pierre & Miquelon'), ('Pitcairn', 'Pitcairn'), ('Puerto', 'Puerto Rico'), ('Portugal', 'Portugal'), ('Palau', 'Palau'), ('Paraguay', 'Paraguay'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Solomon', 'Solomon Islands'), ('Seychelles', 'Seychelles'), ('Sudan', 'Sudan'), ('Sweden', 'Sweden'), ('Singapore', 'Singapore'), ('St. Helena', 'St. Helena'), ('Slovenia', 'Slovenia'), ('Svalbard', 'Svalbard & Jan Mayen Islands'), ('Slovakia', 'Slovakia'), ('Sierra Leone', 'Sierra Leone'), ('San Marin', 'San Marino'), ('Senegal', 'Senegal'), ('Somalia', 'Somalia'), ('Suriname', 'Suriname'), ('Sao Tome & Principe', 'Sao Tome & Principe'), ('El Salvador', 'El Salvador'), ('Syrian', 'Syrian Arab Republic'), ('Swaziland', 'Swaziland'), ('Turks', 'Turks & Caicos Islands'), ('Chad', 'Chad'), ('French', 'French Southern Territories'), ('Togo', 'Togo'), ('Thailand', 'Thailand'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Turkmenistan', 'Turkmenistan'), ('Tunisia', 'Tunisia'), ('Tonga', 'Tonga'), ('East Timor', 'East Timor'), ('Turkey', 'Turkey'), ('Trinidad', 'Trinidad & Tobago'), ('Tuvalu', 'Tuvalu'), ('Taiwan', 'Taiwan, Province of China'), ('Tanzania', 'Tanzania, United Republic of'), ('Ukraine', 'Ukraine'), ('Uganda', 'Uganda'), ('Minor Outlying Islands', 'United States Minor Outlying Islands'), ('US', 'United States of America'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vatican City', 'Vatican City State (Holy See)'), ('St. Vincent & the Grenadines', 'St. Vincent & the Grenadines'), ('Venezuela', 'Venezuela'), ('British Virgin Islands', 'British Virgin Islands'), ('United States Virgin Islands', 'United States Virgin Islands'), ('Viet', 'Viet Nam'), ('Vanuatu', 'Vanuatu'), ('Wallis', 'Wallis & Futuna Islands'), ('Samoa', 'Samoa'), ('Yemen', 'Yemen'), ('Mayotte', 'Mayotte'), ('Yugoslavia', 'Yugoslavia'), ('South Africa', 'South Africa'), ('Zambia', 'Zambia'), ('Zaire', 'Zaire'), ('Zimbabwe', 'Zimbabwe'), ('Unknown', 'Unknown or unspecified country')], default='', max_length=25)),
                ('Phone_Number', models.CharField(blank=True, default='', max_length=20, null=True)),
            ],
        ),
    ]