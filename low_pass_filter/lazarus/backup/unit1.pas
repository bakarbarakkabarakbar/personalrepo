unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, TAGraph, TASeries, Forms, Controls, Graphics,
  Dialogs, StdCtrls,Math;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Chart1: TChart;
    Chart1LineSeries1: TLineSeries;
    Chart2: TChart;
    Chart2LineSeries1: TLineSeries;
    Chart2LineSeries2: TLineSeries;
    Chart2LineSeries3: TLineSeries;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Edit4: TEdit;
    Edit5: TEdit;
    Edit6: TEdit;
    Edit7: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    RadioButton1: TRadioButton;
    RadioButton2: TRadioButton;
    RadioButton3: TRadioButton;
    procedure Button1Click(Sender: TObject);
    procedure RadioButton1Change(Sender: TObject);
    procedure RadioButton2Change(Sender: TObject);
    procedure RadioButton3Change(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  fs,A1,A2,A3,F1,F2,F3,ndata,n: integer;
  Fc,Wc: Extended;
  Sin1,Sin2,Sin3,Input,y,yy,yyy: array [0..1000] of extended;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
  Chart1LIneSeries1.Clear;
  fs:= 1000;
  ndata:= 100;
  A1:= strtoint(Edit1.Text);
  A2:= strtoint(Edit2.Text);
  A3:= strtoint(Edit3.Text);
  F1:= strtoint(Edit4.Text);
  F2:= strtoint(Edit5.Text);
  F3:= strtoint(Edit6.Text);

  for n:=0 to ndata-1 do
  begin
   Sin1[n]:= A1*sin(2*pi*F1*n/fs);
   Sin2[n]:= A2*sin(2*pi*F2*n/fs);
   Sin3[n]:= A3*sin(2*pi*F3*n/fs);

   Input[n]:= Sin1[n] + Sin2[n] + Sin3[n];

   Chart1LineSeries1.AddXY(n,Input[n]);
  end;
end;

procedure TForm1.RadioButton1Change(Sender: TObject);
begin
  Chart2LineSeries1.Clear;
  Chart2LineSeries2.Clear;
  Chart2LineSeries3.Clear;
  fs:= 1000;
  ndata:=100;
  fc:= strtofloat (Edit7.Text);
  wc:= 2*pi*fc;
  for n:=0 to ndata-1 do
  begin
   y[n]:= ((2*fs-wc)*y[n-1]+wc*Input[n]+wc*Input[n-1])/(2*fs+wc);

   Chart2LineSeries1.AddXY(n,y[n]);
  end;
end;

procedure TForm1.RadioButton2Change(Sender: TObject);
begin
  Chart2LineSeries1.Clear;
  Chart2LineSeries2.Clear;
  Chart2LineSeries3.Clear;
  fs:= 1000;
  ndata:= 100;
  wc:=2*pi*fc;
  for n:=0 to ndata-1 do
  begin
    yy[n]:==((((8*sqr(fs))-(2*sqr(Wc)))*yy[n-1])-(((4*sqr(fs))-(2*sqrt(2)*Wc*fs)+sqr(Wc))*yy[n-2])+(sqr(Wc)*Input[n])+(2*sqr(Wc)*Input[n-1])+(sqr(Wc)*Input[n-2]))/((4*sqr(fs))+(2*sqrt(2)*Wc*fs)+sqr(Wc));

    Chart2LineSeries2.AddXY(n,yy[n]);
  end;
end;

procedure TForm1.RadioButton3Change(Sender: TObject);
begin
  Chart2LineSeries1.Clear;
  Chart2LineSeries2.Clear;
  Chart2LineSeries3.Clear;
  fs:= 1000;
  ndata:= 100;
  wc:=2*pi*fc;
  for n:=0 to ndata-1 do
  begin
    yyy[n]:=((((power(Wc,3))*Input[n])+(3*(power(Wc,3))*Input[n-1])+(3*power(Wc,3)*Input[n-2])+((power(Wc,3))*Input[n-3]))+(((24*(power(fs,3)))+(8*Wc*(Power(fs,2)))-(4*(power(Wc,2))*fs)-(3*(power(Wc,3))))*yyy[n-1])-(((24*(power(fs,3)))-(8*Wc*sqr(fs))-(4*(power(Wc,2))*fs)+(3*(power(Wc,3))))*yyy[n-2])+(((8*(power(fs,3)))-(8*Wc*sqr(fs))+(4*sqr(Wc)*fs)-(power(Wc,3)))*yyy[n-3]))/((8*(power(fs,3)))+(8*Wc*sqr(fs))+(4*sqr(Wc)*fs)+(Power(Wc,3)));

    Chart2LineSeries3.AddXY(n,yyy[n]);
  end;
end;

end.

