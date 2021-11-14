unit Unit2;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, dspinterface, math,
  VclTee.TeeGDIPlus, Vcl.StdCtrls, VCLTee.TeEngine, VCLTee.Series,
  Vcl.ExtCtrls, VCLTee.TeeProcs, VCLTee.Chart;

type
  arraybaru = array[-9999..9999] of real;

  TForm2 = class(TForm)
    Button1: TButton;
    Chart1: TChart;
    Series1: TLineSeries;
    Chart2: TChart;
    Series2: TLineSeries;
    Button2: TButton;
    Chart3: TChart;
    LineSeries1: TLineSeries;
    pole1: TLineSeries;
    pole2: TLineSeries;
    horizontal: TLineSeries;
    vertical: TLineSeries;
    zero1: TLineSeries;
    zero2: TLineSeries;
    ScrollBar1: TScrollBar;
    ScrollBar2: TScrollBar;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Chart4: TChart;
    Chart5: TChart;
    mag2chart: TBarSeries;
    MagnitudeChart: TBarSeries;
    procedure Button1Click(Sender: TObject);
    procedure bsf;
    procedure pole;
    procedure ScrollBar1Change(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure ScrollBar2Change(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  y,x : arraybaru;
  r, teta : extended;
  end;

var
  Form2: TForm2;
  i,j,k,n : integer;
  xp1, yp1, xp2, yp2 : extended;
  re1, im1, re2, im2 : arraybaru;
  denum, num : arraybaru;
  magnitude, phase : arraybaru;


implementation



{$R *.dfm}

uses Unit1, Unit3;


{ TForm2 }

procedure TForm2.bsf;
var
  fs : extended;
begin
  series2.Clear;
  magnitudechart.Clear;
  mag2chart.Clear;

  zero1.Clear;
  zero2.Clear;

  r:= scrollbar1.Position/10;
  teta:= scrollbar2.Position*pi/180;

  for i := 1 to form1.jmldataecg do
    begin
      x[i] := form1.xecgfilter[i];
    end;


  for n:= 1 to (form1.jmldataecg) do
  begin
   y[n]:= x[n] - x[n-2] + (2*cos(teta)*r*y[n-1]) - (sqr(r)*y[n-2]);
   series2.AddXY(n, y[n]);
  end;

  fs := form1.fsecg;

  for j:= 0 to round(fs/2) do
   begin
    re1[j] := cos(2*2*pi*j/fs) - 1;
    im1[j] := sin(2*2*pi*j/fs);
    re2[j] := cos(2*2*pi*j/fs) - (2*r*cos(teta)*cos(2*pi*j/fs)) + sqr(r);
    im2[j] := sin(2*2*pi*j/fs) - (2*r*cos(teta)*sin(2*pi*j/fs));
    num[j]:= sqr(re1[j]) + sqr(im1[j]);
    denum[j]:= sqr(re2[j]) + sqr(im2[j]);
    magnitude[j]:= (sqrt(num[j] / denum[j]));
    magnitudechart.AddXY(j, magnitude[j]);
   end;

   for i := 0 to ((form1.datazp div 2)-1) do
     begin
        Mag2chart.AddXY(i*fs/form1.datazp, form1.mag2[i+(form1.datazp div 2)]/2);
     end;

  zero1.AddXY(1,0);
  zero2.AddXY(-1,0);

end;

procedure TForm2.Button1Click(Sender: TObject);
begin
  for i := 1 to form1.jmldataecg do
    begin
      series1.AddXY(i, form1.outhpf[i]);
    end;
end;

procedure TForm2.Button2Click(Sender: TObject);
begin
  bsf;
end;

procedure TForm2.pole;
begin
  pole1.Clear;
  pole2.Clear;

  r:= 0.1*scrollbar1.Position;
  teta:= scrollbar2.Position*pi/180;

  xp1:=r*cos(teta);
  yp1:=r*sin(teta);
  xp2:=r*cos(-teta);
  yp2:=r*sin(-teta);

  pole1.AddXY(xp1,yp1);
  pole2.AddXY(xp2,yp2);

  label2.Caption:= 'R ' + floattostr(r);
  label1.Caption:= 'Teta ' + inttostr(scrollbar2.Position);

end;

procedure TForm2.ScrollBar1Change(Sender: TObject);
begin
  pole;
  bsf;
end;

procedure TForm2.ScrollBar2Change(Sender: TObject);
begin
  pole;
  bsf;
end;

end.

