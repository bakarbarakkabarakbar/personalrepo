unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls, StdCtrls, JPEG, Math;

type

  TStringArray = array of string;
  TIntegerArray = array of Extended;

  TForm1 = class(TForm)
    Button1: TButton;
    Image1: TImage;
    Button2: TButton;
    Button4: TButton;
    OpenDialog1: TOpenDialog;
    Image2: TImage;
    Button3: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);

  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  PixelArray : Array of array of Integer;
  JumlahDataX, JumlahDataY, Alpha : Integer;
  FFTFinal1 : Array of array of Extended;

implementation

{$R *.dfm}

function BitReversal(Input, Alpha:Integer):Integer;
var
  Bin,  BinInverse: Array[0..100] of Integer;
  i,j: Integer;

begin
  //Isi array dengan zero

  for i:=0 to 100 do Bin[i]:=0;
  for i:=0 to 100 do BinInverse[i]:=0;

  i := 0;
  While Input <> 0 do
  begin
    Bin[i] := Input mod 2;
    Input := Input div 2;
    //ShowMessage(IntToStr(Bin[i]));
    //ShowMessage(IntToStr(Input));
    i := i + 1;
    if Input = 1 then
    begin
      Bin[i] := 1;
      Input := Input - 1;
      //ShowMessage(IntToStr(Bin[i]));
    end;
  end;

  For i:=0 to Alpha-1 do
  begin
    BinInverse[i] := Bin[Alpha-1-i];
  end;

  Result:=0;

  For j:=0 to Alpha-1 do
  begin
    Result:=Result + Round(power(2, j)*BinInverse[j]);
  end;
end;

function FFT(Panjang : Integer ;InputArray : TIntegerArray):TIntegerArray;
var
  perulangan : Integer;
  i,j,k,l,m,n: Integer;
  FFTZeroPad : TIntegerArray;
  FFTBitReversal: TIntegerArray;
  re : Array of Extended;
  im : TIntegerArray;

begin
  //ZeroPadding
  Alpha:=0;
  While Panjang > power(2, Alpha) do
  begin
    inc(Alpha);
  end;
  SetLength(FFTZeroPad, Round(power(2, Alpha)));
  SetLength(FFTBitReversal, Round(power(2, Alpha)));
  SetLength(Result, Round(power(2, Alpha)));
  SetLength(re, Round(power(2, Alpha)));
  SetLength(im, Round(power(2, Alpha)));

  For i:=0 to Round(power(2,Alpha))-1 do
  begin
    if i<=Panjang then FFTZeropad[i]:=InputArray[i]
    else FFTZeroPad[i] := 0;
  end;

  //Bit Reversal
  For i:=0 to Round(power(2,Alpha))-1 do
  begin
    FFTBitReversal[i] := FFTZeroPad[BitReversal(i,Alpha)];
    //ShowMessage(FloatToStr(i));
    re[i] :=0;
    im[i] :=0;
  end;

  //Butterfly
  For i:=0 to Alpha-1 do
  begin
    perulangan := round(power(2, Alpha - ( i + 1)));
    n:=perulangan div 2;
    for k:=0 to round(power(2,i))-1 do
    begin
      l:=0;
      for j:=perulangan * k to perulangan * k + perulangan - 1 do
      begin
        if j < (perulangan * k + perulangan div 2) then
        begin
          re[j]:=Round(FFTBitReversal[j]) + Round(FFTBitReversal[j + n]);
        end
        else
        begin
          re[j]:=(FFTBitReversal[j - n] - FFTBitReversal[j]) * cos(2 * pi  * l / power(2, Alpha));
          im[j]:=im[j]-(FFTBitReversal[j - n] - FFTBitReversal[j]) * sin(2 * pi  * l / round(power(2, Alpha)));
          l := round(power(2, i));
        end;
      end;
    end;
    for m:=0 to round(power(2,Alpha))- 1 do
    begin
      FFTBitReversal[m] := sqrt(sqr(re[m]) + sqr(im[m]));
    end;
  end;

  for m:=0 to round(power(2,Alpha))-1 do
    begin
      Result[m] := Round(FFTBitReversal[m]);
    end;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
  OpenDialog1 := TOpenDialog.Create(self);
  OpenDialog1.InitialDir := GetCurrentDir;
  OpenDialog1.Filter := 'File BitMap|*.bmp';

  if not OpenDialog1.Execute then
    ShowMessage('Gagal mengambil file');

  ShowMessage(OpenDialog1.FileName);

  Image1.Picture.LoadFromFile(OpenDialog1.FileName);

  JumlahDataX:=Image1.Picture.Width;
  JumlahDataY:=Image1.Picture.Height;

  OpenDialog1.Free;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  Form1.Close;
end;

procedure TForm1.Button2Click(Sender: TObject);
var
  i,j:Integer;
  GreyscaleINT : Integer;
  Color1 : LongInt;
  R, G, B : Integer;

begin
  Setlength(PixelArray, JumlahDataX, JumlahDataY);
  //ShowMessage(IntToStr(JumlahDataY));
  //ShowMessage(IntToStr(JumlahDataX));

  For i:=0 to JumlahDataY-1 do
  begin
    For j:=0 to JumlahDataX-1 do
    begin
      Color1 := ColorToRGB(Image1.Canvas.Pixels[i,j]);
      //ShowMessage(IntToStr(i));
      R := GetRValue(Color1);
      G := GetGValue(Color1);
      B := GetBValue(Color1);
      //ShowMessage(IntToStr(Color));
      //ShowMessage(IntToStr(B));
      //red := Input[j].R;
      //green := Input[j].G;
      //blue := Input[j].B;
      GreyscaleINT := Round(R * 0.56 + G * 0.33 + B * 0.11);
      PixelArray[i,j]:=GreyscaleINT;
      Image2.Canvas.Pixels[i,j] := RGB(GreyscaleINT, GreyscaleINT, GreyscaleINT);
      //Image2.Canvas.Pixels[i,j] := RGB(GreyscaleINT, GreyscaleINT, GreyscaleINT);
    end;
  end;

end;

procedure TForm1.Button3Click(Sender: TObject);
var
  i, j, k : Integer;
  l:Extended;
  FFTArrayY : TIntegerArray;
  FFTArrayX : TIntegerArray;
  FFTHasilY : TIntegerArray;
  FFTHasilX : TIntegerArray;

begin
  //FFT pada kolom
  SetLength(FFTArrayX, JumlahDataX);
  SetLength(FFTArrayY, JumlahDataY);
  SetLength(FFTHasilX, Round(power(2,Alpha)));
  SetLength(FFTHasilY, Round(power(2,Alpha)));
  SetLength(FFTFinal1, Round(power(2,Alpha)), Round(power(2,Alpha)));

  for i:=0 to JumlahDataX-1 do
  begin
    for j:=0 to JumlahDataY-1 do
    begin
      FFTArrayY[j]:=PixelArray[j,i];
    end;
    FFTHasilY := FFT(JumlahDataY, FFTArrayY);
    for k:=0 to Round(power(2, Alpha))-1 do
    begin
      FFTFinal1[j,i] := FFTHasilY[j];
    end;
  end;

  //FFT pada baris
  for i:=0 to JumlahDataY-1 do
  begin
    for j:=0 to JumlahDataX-1 do
    begin
      FFTArrayX[j]:=PixelArray[i,j];
    end;
    FFTHasilX := FFT(JumlahDataX, FFTArrayX);
    for j:=0 to Round(power(2,Alpha))-1 do
    begin
      FFTFinal1[i,j] := Round(FFTHasilX[j]);
    end;
  end;
  

  //Image2.Height:=Round(power(2,Alpha));
  //Image2.Width:=Round(power(2,Alpha));

  //PLOT FFT
  for i:=0 to JumlahDataX-1 do
  begin
    for j:=0 to JumlahDataY-1 do
    begin
      l:=FFTFinal1[i,j];
      Image2.Canvas.Pixels[i,j] := RGB(round(l), round(l), round(l));
    end;
  end;

end;

end.
