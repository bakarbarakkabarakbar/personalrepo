#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void id_register();
void id_find();
void id_edit();
void id_about();
void delay(unsigned int mseconds);
int calendar(int,int);

struct date
{
    int day;
    int month;
    int year;
}date;

struct id
{
    struct date birthday;
    char firstname[100];
    char lastname[100];
    int number;
}id;

struct past_appointment
{
    char firstname[100];
    char lastname[100];
    struct date date;
    char doctor[100];
    char disease[100];
};

int main()
{
    int number;
        check_1:
    printf("C Program Hospital Database System\n\n");
    printf("\t1. Register ID to Database\n");
    printf("\t2. Find ID Database\n");
    printf("\t3. Edit ID Database\n");
    printf("\t4. About Program\n");
    printf("\t5. Exit Program\n\n");
    printf("Select Number -> ");
    switch(getch())
    {
        case '1':
            id_register();
            system("cls");
            delay(500);
            goto check_1;

        case '2':
            id_find();
            system("cls");
            delay(500);
            goto check_1;
        case '3':
            id_edit();
            system("cls");
            delay(500);
            goto check_1;
        case '4':
            id_about();
            system("cls");
            delay(500);
            goto check_1;
        case '5':
            system("cls");
            printf("Exiting Program.....");
            exit(0);
    }
    return 0;
}

void id_register()
{
    char filename[100];
    int temp;
    FILE*fp;

        check_2:
    printf("Please input data\n\tFirst Name : ");scanf("%s", id.firstname);
    printf("\tLast Name : ");scanf("%s", id.lastname);
    printf("\tBirthday\n\t\tDay : ");scanf("%d", &id.birthday.day);
    printf("\tBirthday\n\t\tMonth : ");scanf("%d", &id.birthday.month);
    printf("\tBirthday\n\t\tYear : ");scanf("%d", &id.birthday.year);
    printf("\tID Number : ");scanf("%d", &id.number);
         check_3:
    printf("Are You Sure (Yes=1/No=0)? ");
    scanf("%d", &temp);

    if(temp==1)
    {
        if((test_date(id.birthday.day,id.birthday.month,id.birthday.year))==1)
        {
            sprintf(filename, "%d.csv", id.number);
            fpointer = fopen(filename, "wx");
            fwrite(&id, sizeof(struct id), 4, fpointer);
            fclose(fpointer);
            system ("cls");
            goto stop;
        }
        else
        {
            printf("Please insert correct number...\n");
            delay(1000);
            system("cls");
            goto check_2;
        }
    }
    else(temp==0);
    {
        goto check_2;
    }
        stop:
    system("cls");
    printf("Data has been recorded!!\n\nReturning to home.....");
    delay(1500);
}

void id_find()
{
    int number, line_length, numtemp1, numtemp2, numtemp3;
    char filename[21], temp[512];
    FILE*fpointer;

    system("cls");
        check_1:
    printf("Option to use as identifier:\n");
    printf("\t1. Use ID Number\n");
    printf("\t2. Use Name and Birthday\n");
    printf("\t3. Cancel\n");
    printf("Select Number -> ");
    scanf("%d", &number);
    if(number==1)
    {
        printf("Please insert ID number : ");
        scanf("%d", &id.number);
        delay(200);
        sprintf(filename, "%d.csv", id.number);
        if((fpointer=fopen(filename, "r"))==NULL)
        {
            printf(" ! The File is Empty or Not Found !!!...\n\n");
            delay(2000);
            system("cls");
            goto check_1;
        }
        fpointer = fopen(filename, "r");
        fread(&id, sizeof(struct id), 4, fpointer);
        printf("\nHere's the following data\n");
        printf("ID number = %d\n", id.number);
        printf("ID Name = %s %s\n", id.firstname, id.lastname);
        printf("Birthday = %d %d %d\n", id.birthday.day, id.birthday.month, id.birthday.year);
        printf("\t%s's Previous Check Up\n", id.lastname);

        if(feof(fpointer))
        {
            printf("\t%s's Last Appointment\n", id.lastname);
            while(1)
            {

            }
            printf("\n\t%s's Upcoming Appointment\n", id.lastname);

            while(1)
            {

            }
        }
        else
        {
            printf("\t%s's doesn't have any appointment!!...\n");
        }

        delay(500);
        printf("\nPlease select option :\n");
        printf("\t1. Book new appointment\n");
        printf("\t2. Search other ID database\n");
        printf("\t3. Return to home\nSelect Number -> ");
        scanf("%d", &number);
        if(number==1)
        {
            printf("Please select date of new appointment ...\n");
            printf("Please enter a date\n\tYear (example: 1999) : ");
            scanf("%d", &numtemp1);
            printf("\tMonth (1-12): ");
            scanf("%d", &numtemp2);
            calendar(numtemp1,numtemp2);
            delay(2000);
            printf("Please enter date : ");
            scanf("%d", &numtemp3);
            printf("Please select doctor for :");

        }
        if(number==2)
        {
            printf("\nPlease Wait ....");
            delay(200);
            system("cls");
            goto check_1;
        }
        if(number==3)
        {
            goto stop;
        }
    }
    if(number==2)
    {

    }
    if(number==3)
    {
        goto stop;
    }
    if(number!=1&&2&&3)
    {
        printf("Please input correct number...");
        delay(1000);
        system("cls");
        goto check_1;
    }
        stop:
    printf("Returning Home......");
    delay(1000);
    system("cls");
}

void id_edit()
{
    printf("a");
}

void id_about()
{
    printf("a");
}

void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}

int test_date(int d, int m, int y)
{
    int daysinmonth[12]={31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int a = 0;

    if(y % 400 == 0 || (y % 100 != 0 && y % 4 == 0))
    daysinmonth[1]=29;

    if (m<13)
    {
        if( d <= daysinmonth[m-1] )
        a=1;
        return a;
    }
    else
    {
        return a;
    }
}

int calendar(int year, int month)
{
    int days_in_month[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    char *months[]={"January","February","March","April","May","June","July","August","September","October","November","December"};

	int daycode, day, d1, d2, d3;

	d1 = (year - 1.)/ 4.0;
	d2 = (year - 1.)/ 100.;
	d3 = (year - 1.)/ 400.;
	daycode = (year + d1 - d2 + d3) %7;

	if(year% 4 == 0 && year%100 != 0 || year%400 == 0)
	{
		days_in_month[2] = 29;
    }
	else
	{
		days_in_month[2] = 28;
	}

    printf("%s", months[month-1]);
    printf("\nSun  Mon  Tue  Wed  Thu  Fri  Sat\n" );

    for ( day = 1; day <= 1 + daycode * 5; day++ )
    {
        printf(" ");
    }
    for ( day = 1; day <= days_in_month[month]; day++ )
    {
		printf("%2d", day );
		if ( ( day + daycode ) % 7 > 0 )
			{printf("   " );}
		else
            {printf("\n " );}
    }
    return 0;
}
