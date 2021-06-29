unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Math, TeEngine, TeeFunci, Series, ExtCtrls, TeeProcs,
  Chart;

type
  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    OpenDialog1: TOpenDialog;
    Memo1: TMemo;
    Button4: TButton;
    RadioButton1: TRadioButton;
    RadioButton2: TRadioButton;
    Chart1: TChart;
    Series1: TLineSeries;
    Chart2: TChart;
    Series2: TLineSeries;
    Chart3: TChart;
    Series3: TLineSeries;
    procedure Button3Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  XData, ECG1, ECG2, ECG: Array[0..10000] of Extended;
  JumlahData, FrekuensiSampling: Integer;
  HannWindowing: Array[0..10000] of Extended;
  HasilFT, DataFT:Array[0..10000] of Extended;

implementation

{$R *.dfm}

procedure Delay(dwMilliseconds: Longint);
var
  iStart, iStop: DWORD;
begin
  iStart := GetTickCount;
  repeat
    iStop := GetTickCount;
    Application.ProcessMessages;
    Sleep(1); // addition from Christian Scheffler to avoid high CPU last
  until (iStop - iStart) >= dwMilliseconds;
end;

function FourierTransform:Extended;
var
  ii, jj, kk, ll, mm, nn: Extended;
  i,j,k,l,m,n: Integer;
begin
  //for i:=0 to 400-1 do
  //begin
  //  DataFT[i] := DataFT[i+1];
  //end;
  //DataFT[400-1]:=Masukan;

  for i:=0 to 400-1 do
  begin
    ii:=0;
    jj:=0;
    for j:=0 to 400-1 do
    begin
      ii:=ii + DataFT[j] * cos(2 * pi * i * j / 400-1);
      jj:=jj - DataFT[j] * sin(2 * pi * i * j / 400-1);
    end;
    HasilFT[i]:=sqrt(sqr(ii) + sqr(jj));
  end;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  Form1.close;
end;

procedure TForm1.Button1Click(Sender: TObject);
var
  Data1: TStringList;
  Data2: TStringList;
  ii, jj, kk, ll, mm, nn: Extended;
  i,j,k,l,m,n: Integer;
  fmt: TFormatSettings;

begin
  //MENGGANTI DENUMERATOR
  //SystemDecimalSep := SysUtils.FormatSettings.DecimalSeparator;
  //SysUtils.FormatSettings.DecimalSeparator := '.';
  //Application.UpdateFormatSettings := False; //block refreshing format settings

  //MENDAPATKAN LOKASI FILE
  OpenDialog1 := TOpenDialog.Create(self);
  OpenDialog1.InitialDir := GetCurrentDir;
  openDialog1.Filter := 'Text Files|*.txt';

  if not OpenDialog1.Execute then
    ShowMessage('Tidak ada File yang di Pilih');

  Memo1.Lines.LoadFromFile(OpenDialog1.FileName);

  //MENCARI FREKUENSI SAMPLING DARI FILE TEXT

  Data1 := TStringList.Create;
  ExtractStrings([#9], [], PChar(Memo1.Lines[1]), Data1);
  Data1[0] := StringReplace(Data1[0], '(', '', [rfReplaceAll]);
  Data1[0] := StringReplace(Data1[0], ')', '', [rfReplaceAll]);
  Data1[0] := StringReplace(Data1[0], 'sec', '', [rfReplaceAll]);

  FrekuensiSampling := round(1/StrToFloat(Data1[0]));

  for i := 2 to Memo1.Lines.Count-1 do
  begin
    Data1 := TStringList.Create;
    ExtractStrings([#9], [], PChar(Memo1.Lines[i]), Data1);
    XData[i-3] := StrToFloat(Data1[0]);
    ECG1[i-3] := StrToFloat(Data1[1]);
    ECG2[i-3] := StrToFloat(Data1[2]);
    JumlahData := Round(StrToFloat(Data1[0]));
  end;

  //ShowMessage(Data2[0]);

  //Data[1]  := StringReplace(Data[1], ' ', '', [rfReplaceAll, rfIgnoreCase]);

  //While Pos(#9,Data[1]) do
  //  Data[1][Pos(39,Str)]:='';

  //ii := StrToFloat(Trim(Data[0])) * StrToFloat(Trim(Data[1]));
  //OutputDialog := FloatToStr(ii);

end;

procedure TForm1.Button4Click(Sender: TObject);
var
  ii, jj, kk, ll, mm, nn: Extended;
  i,j,k,l,m,n: Integer;
  PeriodeSampling: Integer;

begin
  //PEMILIHAN JENIS DATA
  Series1.Clear;
  if RadioButton1.Checked then ECG := ECG1;
  if RadioButton2.Checked then ECG := ECG2;

  PeriodeSampling := round(1/FrekuensiSampling);

  j:=0;

  //MEMBENTUK HANN WINDOWING
  For i:=0 to 400 do
    HannWindowing[i] := 0.5 - 0.5 * cos((2 * pi * i) / (400 - 1));

  //PLOT DATA PADA GRAFIK DENGAN MENGGUNAKAN FREKUENSI SAMPLING
  for i:=0 to JumlahData do
  begin
    if j >= 400 then
    begin
    j:=0;

    FourierTransform();
    Series3.Clear;
    For k:=0 to JumlahData do Series3.AddXY(XData[k], HasilFT[k]);

    end;
    if i >= 400 then
    begin
      Series1.Delete(j);
      Series2.Delete(j);
    end;

    DataFT[j]:=ECG[i]*HannWindowing[j];

    Series1.AddXY(XData[j], ECG[i]);
    Series2.AddXY(XData[j], ECG[i]*HannWindowing[j]);
    Delay(PeriodeSampling*1000);
    j:=j+1;
  end;
end;

end.




