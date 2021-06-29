#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>
#include <string.h>

    // deklarasi struct dan grobal variabel

struct date
{
    int day;
    int month;
    int year;
}date;

struct id
{
    struct date bday;
    char name[100];
    int num;
}id;

struct doctor
{
    int age;
    char name[100];
    char departemen[100];
}doc;

struct apt
{
    int num;
    struct id id;
    struct doctor doc;
    struct date date;
}apt;

FILE*fp;
FILE*fq;
char a[100],b[100];
int tempd[100], idnum[100], x, y, z;


int main();
void book_appointment();
void appointment();

    // deklarasi fungsi

void show_calendar(struct date date)
{
    int days[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    const char *months[12]={"January","February","March","April","May","June","July","August","September","October","November","December"};
    if(date.year% 4 == 0 && date.year%100 != 0 || date.year%400 == 0){
        days[2] = 29;
    }
    else{
        days[2] = 28;
    }

    printf("\t\t%s\n", months[date.month-1]);

    tempd[4]=0;
    for(tempd[3]=1;tempd[3]<=days[date.month];tempd[3]++){
        printf("%d\t", tempd[3]);
        tempd[4]++;
        if(tempd[4]==7){
            printf("\n");
            tempd[4]=0;
        }
    }
}

int t_date(struct date date)
{
    int days[12]={31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int a = 0;

    if(date.year % 400 == 0 || (date.year % 100 != 0 && date.year % 4 == 0)){
        days[1]=29;
    }

    if(date.month<13){
        if(date.day<=days[date.month-1]){
            a=1;
            return a;
        }
        else{
            return a;
        }
    }
    else{
        return a;
    }
}

void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}

void doc1()
{
    printf("\nSelect a doctor's department\n");
    printf("1. Cardiology\n");
    printf("2. Care\n");
    printf("3. Radiology\n");
    printf("4. Rehabilitation\n");
    printf("5. Return\n");
    scanf("%s", a);

    printf("List %s Doctor :\n",a);
    fp = fopen("doc.txt", "r");
    while(1){
        fread(&doc,sizeof(struct doctor), 1, fp);
        if(strcmp(a, doc.departemen)==0){
            printf(" Nama : %s Departemen : %s Umur : %d\n", doc.name, doc.departemen, doc.age);
        }
        if(feof(fp)){
            break;
        }
    }
    rewind(fp);

    printf("Pilih nama dokter :");
    while(getchar() != '\n');
    fgets(a,100,stdin);
    while(1){
        fread(&doc,sizeof(struct doctor), 1, fp);
        if(strcmp(a, doc.name)==0){
            break;
        }
        if(feof(fp)){
            printf("Ada kesalahan, silahkan coba lagi");
            appointment();break;
        }
    }
}

void book_appointment()
{
    printf("Masukkan tanggal");
    printf("\n\t- Hari : ");scanf("%d", &date.day);
    printf("\t- Bulan : ");scanf("%d", &date.month);
    printf("\t- Tahun : ");scanf("%d", &date.year);

    if(t_date(date)){
        show_calendar(date);
    }
    else{
        printf("\nMasukkan tanggal secara benar!!");book_appointment();
    }

    doc1();
    system("cls");

    printf("Nomer ID : %d\n\n", id.num);
    printf("Nama ID : %s\n",id.name);
    printf("Ulang Tahun : %d %d %d\n", id.bday);
    printf("Nama Dokter : %s\n", doc.name);
    printf("Umur Dokter : %d\n\n", doc.age);
    printf("Tanggal : %d %d %d", date);
    printf("Tekan 1 Untuk melanjutkan, Tekan 0 untuk batal\n");

    switch(getch()){
    case '1':
        tempd[0]=0;tempd[1]=1;
        fp = fopen("apt.txt", "r");
        while(1){
            fread(&apt,sizeof(struct apt),1,fp);
            if((strcmp(apt.id.name,id.name)==0)&&(strcmp(apt.doc.name,doc.name)==0)&&apt.date.day==date.day&&apt.date.month==date.month&&apt.date.year==date.year){
                tempd[0]++;
            }
            if(tempd[0]>=2){
                printf("Jadwal untuk dokter %s telah terpenuhi\n");
                delay(1000);
                main();break;
            }
            if(feof(fp)){
                apt.num=tempd[1];
                apt.id.bday.day=id.bday.day;
                apt.id.bday.month=id.bday.month;
                apt.id.bday.year=id.bday.year;
                apt.date.day=date.day;
                apt.date.month=date.month;
                apt.date.year=date.year;
                strcpy(apt.id.name,id.name);
                apt.id.num=id.num;
                strcpy(apt.doc.name,doc.name);
                apt.doc.age=doc.age;

                fclose(fp);fp = fopen("apt.txt", "a");
                fwrite(&apt,sizeof(struct apt),1,fp);fclose(fp);
                printf("Appointment berhasil, Kembali ke halaman utama");
                delay(1000);main();
                main();break;
            }
            tempd[1]++;
        }
    case '2':
        main();break;
    }
}

void find_appointment()
{
    printf("No.\tNama ID\tNama Dokter\tTanggal\n");
    fp = fopen("apt.txt", "r");
    tempd[0]=0;
    while(1){
        if(feof(fp)){
            if(tempd[0]==0){
                printf("not found!!!\n\n");
            }
            appointment();
        }
        if(id.num==apt.id.num){
            tempd[0]++;
            printf("%d\t%s\t%s\t%d-%d-%d\n", apt.num, apt.id.name, apt.doc.name, apt.date.day, apt.date.month, apt.date.year);
        }
        fread(&apt,sizeof(struct apt), 1, fp);
    }
}

void appointment()
{
    printf("1. Buat pertemuan baru\n");
    printf("2. Cek pertemuan yang ada\n");
    printf("3. Kembali\n");
    switch(getch()){
    case '1':
        book_appointment();
        system("cls");
        return;
    case '2':
        find_appointment();
        return;
    case '3':
        system("cls");
        main();
        return;
    }
}

void register_id()
{
    printf("Masukkan data\n");
    printf("\tName : ");
    while(getchar() != '\n');
    fgets(id.name,100,stdin);
    printf("\n\tHari Ulang Tahun\n");
    printf("\t- Hari : ");
    scanf("%d", &id.bday.day);
    printf("\t- Month : ");
    scanf("%d", &id.bday.month);
    printf("\t- Year : ");
    scanf("%d", &id.bday.year);
    printf("\n\tNo ID : ");
    scanf("%d", &id.num);
    printf("\nTekan 1 untuk melanjutkan, tekan 0 untuk batal\n");
    switch(getch()){
        case '1':
            sprintf(a, "%d.txt", id.num);
            if(fp = fopen(a, "r")){
                printf("No ID telah digunakan\n");
                delay(1000);
                system("cls");
                return;
            }
            if(t_date(id.bday)){
                fp = fopen(a, "w");
                fwrite(&id, sizeof(struct id), 4, fp);
                fclose(fp);
                fp = fopen("id.txt", "a");
                fprintf(fp,"%d ", id.num);
                fclose(fp);
                printf("ID telah ditambahkan\n");
                delay(1000);
                system("cls");
                return;
            }
            else{
                printf("Ada kesalahan input data");
                delay(1000);
                return;
            }
        case '0':
            system("cls");
            return;
    }
}

void find_id()
{
    printf("Cari berdasarkan :\n");
    printf("  1. Nomer ID\n");
    printf("  2. Nama dan ulang tahun\n");
    switch(getch()){
        case '1':
            system("cls");
            printf("Masukkan nomer ID : ");
            scanf("%d", &tempd[0]);
            sprintf(a,"%d.txt",tempd[0]);
            if(fp = fopen(a, "r")){
                system("cls");
                fread(&id, sizeof(struct id),1,fp);fclose(fp);
                printf("\nID ditemukan\n");
                printf("\tNomer ID : %d\n", id.num);
                printf("\tNama : %s\n",id.name);
                printf("\tUlang tahun : %d %d %d\n", id.bday);
                appointment();
                return;
            }
            else{
                printf("\nID tidak ditemukan");
                delay(1000);
                system("cls");
                return;
            }
        case '2':
            system("cls");
            printf("Masukkan\n");
            printf("\tNama : ");
            while(getchar() != '\n');
            fgets(a,100,stdin);
            printf("\n\tTanggal ulang tahun\n");
            printf("\t- Hari : ");
            scanf("%d",&tempd[0]);
            printf("\t- Bulan : ");
            scanf("%d",&tempd[1]);
            printf("\t- Tahun : ");
            scanf("%d",&tempd[2]);

            fp = fopen("id.txt", "r");
            while(fscanf(fp,"%d",&tempd[3])){
                sprintf(b,"%d.txt",tempd[3]);
                if(fq = fopen(b, "r")){
                    fread(&id, sizeof(struct id), 1, fq);
                    if(((strcmp(a,id.name))==0)&&id.bday.day==tempd[0]&&id.bday.month==tempd[1]&&id.bday.year==tempd[2]){
                        fclose(fp);
                        fclose(fq);
                        printf("\n\nID ditemukan\n");
                        appointment();
                        return;
                    }
                }
                if(feof(fp)){
                    printf("\nID tidak ditemukan");
                    delay(2000);
                    system("cls");
                    return;
                }
            }
    }
}

int main()
{
    int number;
    printf("1. Daftar ID baru\n");
    printf("2. Cari ID\n");
    printf("3. Periksa Jadwal\n");
    printf("4. Periksa Dokter\n");
    printf("5. Edit data\n");
    printf("6. Keluar\n");
    switch(getch())
    {
        case '1':
            system("cls");
            register_id();
            main();
            break;
        case '2':
            system("cls");
            find_id();
            main();
            break;
        case '6':
            system("cls");
            exit(0);
    }
    return 0;
}
