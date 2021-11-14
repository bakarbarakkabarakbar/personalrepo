unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls, TeeProcs, TeEngine, Chart, Series, Math, Unit2;

type
  TForm1 = class(TForm)
    Button1: TButton;
    RadioGroup1: TRadioGroup;
    RadioButton1: TRadioButton;
    Memo1: TMemo;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Edit4: TEdit;
    RadioButton2: TRadioButton;
    OpenDialog1: TOpenDialog;
    Chart1: TChart;
    Chart2: TChart;
    Chart3: TChart;
    Chart4: TChart;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    RadioButton3: TRadioButton;
    RadioButton4: TRadioButton;
    Series1: TFastLineSeries;
    Series4: TFastLineSeries;
    Series2: TPointSeries;
    Series3: TBarSeries;
    Series5: TFastLineSeries;
    Series6: TFastLineSeries;
    OpenDialog2: TOpenDialog;
    Button5: TButton;
    Button6: TButton;
    Button7: TButton;
    RadioButton5: TRadioButton;
    Button8: TButton;
    Button9: TButton;
    Button10: TButton;
    Button11: TButton;
    Button12: TButton;
    Button13: TButton;
    GroupBox1: TGroupBox;
    Series7: TFastLineSeries;
    Series8: TFastLineSeries;
    Series9: TFastLineSeries;
    Series10: TFastLineSeries;
    Series11: TFastLineSeries;
    GroupBox3: TGroupBox;
    GroupBox4: TGroupBox;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    GroupBox5: TGroupBox;
    Button14: TButton;
    Button15: TButton;
    Button16: TButton;
    Button17: TButton;
    Edit5: TEdit;
    Label5: TLabel;
    Label6: TLabel;
    Edit6: TEdit;
    procedure Button1Click(Sender: TObject);
    procedure RadioButton1Click(Sender: TObject);
    procedure RadioButton2Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure RadioButton3Click(Sender: TObject);
    procedure RadioButton4Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure RadioButton5Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
    procedure Button6Click(Sender: TObject);
    procedure Button7Click(Sender: TObject);
    procedure Button8Click(Sender: TObject);
    procedure Button9Click(Sender: TObject);
    procedure Button10Click(Sender: TObject);
    procedure Button11Click(Sender: TObject);
    procedure Button12Click(Sender: TObject);
    procedure Button13Click(Sender: TObject);
    procedure Button16Click(Sender: TObject);
    procedure Button17Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  jumlahinputneuron, jumlahhiddenneuron1, jumlahhiddenneuron2, jumlahoutputneuron: Integer;
  inputlayer : Array[0..1, 0..100] of Extended; //PosisiInput, SequenceInput
  outputlayer : Array[0..6, 0..100] of Extended; //PosisiOutput, Sequence Input
  hiddenlayer : Array[0..2, 0..20] of Extended; //PosisiHiddenLayer, PosisiNeuronnya
  tresholdlayer : Array[0..3] of Extended; //PosisiLayer
  weight : Array[0..2, 0..20, 0..20] of Extended; //PosisiWeight, Neuron Asal, Neuron Tujuan
  jumlahdata : Integer;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
  Memo1.Clear;
  Memo1.Lines.Add('ANN MLP EPBA Gait Phase');
  Memo1.Lines.Add('by : Muhammad Akbar Maulana');
  Memo1.Lines.Add('07311740000015');
end;

procedure TForm1.RadioButton1Click(Sender: TObject);
begin
  Memo1.Clear;

  inputlayer[0][0]:=0;
  inputlayer[1][0]:=0;
  outputlayer[0][0]:=0;

  inputlayer[0][1]:=1;
  inputlayer[1][1]:=0;
  outputlayer[0][1]:=1;

  inputlayer[0][2]:=0;
  inputlayer[1][2]:=1;
  outputlayer[0][2]:=1;

  inputlayer[0][3]:=1;
  inputlayer[1][3]:=1;
  outputlayer[0][3]:=0;

  jumlahdata:=4;

  Memo1.Lines.Add('XOR Neural Network Has Been Selected!!');
  Memo1.Lines.Add('Total Data = '+inttostr(jumlahdata));
  Memo1.Lines.Add('Please Continue By Clicking No 1 Button');
end;

procedure TForm1.RadioButton2Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  Memo1.Clear;
  Memo1.Lines.Add('Gait Phase Neural Network Has Been Selected!!');
  ShowMessage('Select Training Data');

  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        //Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else
      begin
        ReadLn(myFile, inputlayer[0][i-1], inputlayer[1][i-1], outputlayer[0][i-1]);
        Inc(i);
        //Memo1.Lines.Add(floattostr(inputlayer[0][i-1])+floattostr(inputlayer[1][i-1])+floattostr(outputlayer[0][i-1]));
      end;
    end;

    for n := 0 to jumlahdata do
    begin
      Series4.AddXY(n, inputlayer[0][n]);
      Series5.AddXY(n, inputlayer[1][n]);
      Series6.AddXY(n, outputlayer[0][n]);
    end;

    ShowMessage('File Import Complete');
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;
end;

procedure TForm1.RadioButton3Click(Sender: TObject);
begin
  Memo1.Clear;

  inputlayer[0][0]:=0;
  inputlayer[1][0]:=0;
  outputlayer[0][0]:=0;

  inputlayer[0][1]:=1;
  inputlayer[1][1]:=0;
  outputlayer[0][1]:=0;

  inputlayer[0][2]:=0;
  inputlayer[1][2]:=1;
  outputlayer[0][2]:=0;

  inputlayer[0][3]:=1;
  inputlayer[1][3]:=1;
  outputlayer[0][3]:=1;

  jumlahdata:=4;

  Memo1.Lines.Add('AND Neural Network has been selected!!');
  Memo1.Lines.Add('Total Data = '+inttostr(jumlahdata));
  Memo1.Lines.Add('Please Continue By Clicking No 1 Button');
end;

procedure TForm1.RadioButton4Click(Sender: TObject);
begin
  Memo1.Clear;

  inputlayer[0][0]:=0;
  inputlayer[1][0]:=0;
  outputlayer[0][0]:=0;

  inputlayer[0][1]:=1;
  inputlayer[1][1]:=0;
  outputlayer[0][1]:=1;

  inputlayer[0][2]:=0;
  inputlayer[1][2]:=1;
  outputlayer[0][2]:=1;

  inputlayer[0][3]:=1;
  inputlayer[1][3]:=1;
  outputlayer[0][3]:=1;

  jumlahdata:=4;

  Memo1.Lines.Add('OR Neural Network has been selected!!');
  Memo1.Lines.Add('Total Data = '+inttostr(jumlahdata));
  Memo1.Lines.Add('Please Continue With Clicking Number 1 Button');
end;

procedure TForm1.RadioButton5Click(Sender: TObject);
begin
  Memo1.Clear;
  Memo1.Lines.Add('Gait Phase Neural Network Has Been Selected!!');
  ShowMessage('Select Training Data by Clicking Button Below, CAREFULL TO CHOOSE THE INPUT AND OUTPUT NEURON');
end;

procedure TForm1.Button1Click(Sender: TObject);
var
  j, k : Integer;
begin
  jumlahinputneuron:=strtoint(Edit1.text);
  jumlahhiddenneuron1:=strtoint(Edit2.text);
  jumlahhiddenneuron2:=strtoint(Edit3.text);
  jumlahoutputneuron:=strtoint(Edit4.text);
  
  Memo1.Clear;
  Memo1.Lines.Add('Initialization Weight Using Random Gaussian Number');
  Memo1.Lines.Add('Total Input Neuron = '+inttostr(jumlahinputneuron));
  Memo1.Lines.Add('Total Hidden Neuron 1 = '+inttostr(jumlahhiddenneuron1));
  Memo1.Lines.Add('Total Hidden Neuron 2 = '+inttostr(jumlahhiddenneuron2));
  Memo1.Lines.Add('Total Output Neuron = '+inttostr(jumlahoutputneuron));  

  // First Weight
  Memo1.Lines.Add('Layer Pertama');
  for j := 0 to jumlahinputneuron-1 do
    for k := 0 to jumlahhiddenneuron1-1 do
    begin
      weight[0][j][k]:=RandG(0, 0.5);
      Memo1.Lines.Add(floattostr(weight[0][j][k]));
    end;

  //Second Weight
  Memo1.Lines.Add('Layer Kedua');
  for j := 0 to jumlahhiddenneuron1-1 do
    for k := 0 to jumlahhiddenneuron2-1 do
    begin
      weight[1][j][k]:=RandG(0, 0.5);
      Memo1.Lines.Append(floattostr(weight[1][j][k]));
    end;

  //Third Weight
  Memo1.Lines.Add('Layer Ketiga');
  for j := 0 to jumlahhiddenneuron2-1 do
    for k := 0 to jumlahoutputneuron-1 do
    begin
      weight[2][j][k]:=RandG(0, 0.5);
      Memo1.Lines.Add(floattostr(weight[2][j][k]));
    end;

  tresholdlayer[1] := 0.1;
  tresholdlayer[2] := 0.1;
  tresholdlayer[3] := 0.1;
  
end;

procedure TForm1.Button2Click(Sender: TObject);
var
  n, j, k, iteration, iterationlimit: Integer;
  konstantabelajar, erroroutput, errortarget, temporary, sumsquareerror : Extended;
  neuronlayer, error, deltaerror : Array [0..4,0..10] of Extended; //Posisi Layer, Posisi Neuron

begin
  Memo1.Clear;
  //Inisialisasi Konstanta Yang Dibutuhkan
  konstantabelajar := 0.125;
  errortarget := strtofloat(Edit5.Text);
  sumsquareerror := 0;
  iteration := 0;
  iterationlimit := strtoint(Edit6.Text);

  //Repeat Until untuk pembanding erroroutput dengan errortarget
  repeat
  begin
    if iteration > iterationlimit then Break;
    sumsquareerror := 0;

    for n := 0 to jumlahdata-1 do
    begin
      //Mencari Value dari Neuron
      //First Layer adalah Input Layer
      neuronlayer[0][0] := inputlayer[0][n];
      neuronlayer[0][1] := inputlayer[1][n];

      //Second Layer
      for j := 0 to jumlahhiddenneuron1-1 do
      begin
        temporary := 0;
        for k := 0 to jumlahinputneuron-1 do
        begin
          temporary := temporary+neuronlayer[0][k]*weight[0][k][j];
        end;
        temporary := temporary - tresholdlayer[1];
        neuronlayer[1][j] := 1/(1+exp(-temporary));
      end;

      //Third Layer
      for j := 0 to jumlahhiddenneuron2-1 do
      begin
        temporary := 0;
        for k := 0 to jumlahhiddenneuron1-1 do
        begin
          temporary := temporary+neuronlayer[1][k]*weight[1][k][j];
        end;
        temporary := temporary - tresholdlayer[2];
        neuronlayer[2][j] := 1/(1+exp(-temporary));
      end;

      //Fourth Layer
      for j := 0 to jumlahoutputneuron-1 do
      begin
        temporary := 0;
        for k := 0 to jumlahhiddenneuron2-1 do
        begin
          temporary := temporary+neuronlayer[2][k]*weight[2][k][j];
        end;
        temporary := temporary - tresholdlayer[3];
        neuronlayer[3][j] := 1/(1+exp(-temporary));
      end;

      //FeedBackwardPropagationAlgoritm
      //MencariErrorValue
      //Fourth Layer
      //OutputLayer
      for j := 0 to jumlahoutputneuron-1 do
      begin
        error[3][j] := outputlayer[j][n]-neuronlayer[3][j];
        deltaerror[3][j] := error[3][j]*neuronlayer[3][j]*(1-neuronlayer[3][j]);
        sumsquareerror := sumsquareerror + 0.5*sqr(error[3][j]);
      end;

      //ThirdLayer
      for j := 0 to jumlahhiddenneuron2-1 do
      begin
        temporary := 0;
        for k := 0 to jumlahoutputneuron-1 do
        begin
          temporary := temporary+weight[2][j][k]*error[3][k];
        end;
        error[2][j] := temporary;
        deltaerror[2][j] := error[2][j]*neuronlayer[2][j]*(1-neuronlayer[2][j]);
      end;

      //SecondLayer
      for j := 0 to jumlahhiddenneuron1-1 do
      begin
        temporary := 0;
        for k := 0 to jumlahhiddenneuron2-1 do
        begin
          temporary := temporary+weight[1][j][k]*error[2][k];
        end;
        error[1][j] := temporary;
        deltaerror[1][j] := error[1][j]*neuronlayer[1][j]*(1-neuronlayer[1][j]);
      end;

      //FirstLayer
      for j := 0 to jumlahinputneuron-1 do
      begin
        temporary := 0;
        for k := 0 to jumlahhiddenneuron1-1 do
        begin
          temporary := temporary+weight[0][j][k]*error[1][k];
        end;
        error[0][j] := temporary;
        deltaerror[0][j] := error[0][j]*neuronlayer[0][j]*(1-neuronlayer[0][j]);
      end;

      //Mencari Nilai Weight dan Treshold
      //Treshold Output Layer

      for j := 0 to jumlahoutputneuron-1 do
      begin
        tresholdlayer[3] := tresholdlayer[3]-konstantabelajar*deltaerror[3][j];
      end;

      //Third Weight
      for j := 0 to jumlahhiddenneuron2-1 do
      begin
        for k := 0 to jumlahoutputneuron-1 do
        begin
          weight[2][j][k] := weight[2][j][k]+konstantabelajar*deltaerror[3][k]*neuronlayer[2][j];
        end;
        //Treshold Third Layer
        tresholdlayer[2] := tresholdlayer[2]-konstantabelajar*deltaerror[2][j];
      end;

      //Second Weight
      for j := 0 to jumlahhiddenneuron1-1 do
      begin
        for k := 0 to jumlahhiddenneuron2-1 do
        begin
          weight[1][j][k] := weight[1][j][k]+konstantabelajar*deltaerror[2][k]*neuronlayer[1][j];
        end;
        //Treshold Second Layer
        tresholdlayer[1] := tresholdlayer[1]-konstantabelajar*deltaerror[1][j];
      end;

      //First Weight
      for j := 0 to jumlahinputneuron-1 do
      begin
        for k := 0 to jumlahhiddenneuron1-1 do
        begin
          weight[0][j][k] := weight[0][j][k]+konstantabelajar*deltaerror[1][k]*neuronlayer[0][j];
        end;
      end;
    end;
    inc(iteration);

    Memo1.Clear;
    Memo1.Lines.Add('SSE Value : '+floattostr(sumsquareerror));
    Memo1.Lines.Add('Iteration Value : '+inttostr(iteration));
    Series1.AddXY(iteration, sumsquareerror);
  end;
  until sumsquareerror < errortarget;
end;

procedure TForm1.Button3Click(Sender: TObject);
var
  n, i, j, k : Integer;
  temporary : Extended;
  my : TextFile;
begin
  Series4.Clear;
  Series5.Clear;
  Series6.Clear;
  Series7.Clear;
  Series8.Clear;
  Series9.Clear;
  Series10.Clear;
  Series11.Clear;

  if RadioButton1.Checked then
  begin
    Series2.AddXY(inputlayer[0][0], inputlayer[1][0],'0',clRed);
    Series2.AddXY(inputlayer[0][1], inputlayer[1][1],'1',clBlue);
    Series2.AddXY(inputlayer[0][2], inputlayer[1][2],'1',clBlue);
    Series2.AddXY(inputlayer[0][3], inputlayer[1][3],'0',clRed);

    Memo1.Lines.Add('Running Program Using XOR Input');
    Memo1.Lines.Add('Neuron Value:');
  end;

  if RadioButton2.Checked or RadioButton5.Checked then
  begin
    openDialog2 := TOpenDialog.Create(self);
    openDialog2.InitialDir := GetCurrentDir;
    openDialog2.Options := [ofFileMustExist];
    openDialog2.Filter := 'Gait Phase Data|*.dat';
    ShowMessage('Select Input Data');
    if openDialog2.Execute then
    begin
      AssignFile(my, OpenDialog2.FileName);
      Reset(my);

      i := 0;
      while not EOF(my) do
      begin
      if i = 0 then
        begin
          ReadLn(my, jumlahdata);
          //Memo1.Lines.Add(inttostr(jumlahdata));
          Inc(i);
        end else
        begin
          ReadLn(my, inputlayer[0][i-1], inputlayer[1][i-1], outputlayer[0][i-1]);
          Inc(i);
          //Memo1.Lines.Add(floattostr(inputlayer[0][i-1])+floattostr(inputlayer[1][i-1])+floattostr(outputlayer[0][i-1]));
        end;
      end;
    end;
    Memo1.Lines.Add('Running Program Using Gait Phase Input');
    Memo1.Lines.Add('Neuron Value:');
  end;

  if RadioButton3.Checked then
  begin
    Series2.AddXY(inputlayer[0][0], inputlayer[1][0],'0',clRed);
    Series2.AddXY(inputlayer[0][1], inputlayer[1][1],'0',clRed);
    Series2.AddXY(inputlayer[0][2], inputlayer[1][2],'0',clRed);
    Series2.AddXY(inputlayer[0][3], inputlayer[1][3],'1',clBlue);

    Memo1.Lines.Add('Running Program Using AND Input');
    Memo1.Lines.Add('Neuron Value:');
  end;

  if RadioButton4.Checked then
  begin
    Series2.AddXY(inputlayer[0][0], inputlayer[1][0],'0',clRed);
    Series2.AddXY(inputlayer[0][1], inputlayer[1][1],'1',clBlue);
    Series2.AddXY(inputlayer[0][2], inputlayer[1][2],'1',clBlue);
    Series2.AddXY(inputlayer[0][3], inputlayer[1][3],'1',clBlue);

    Memo1.Lines.Add('Running Program Using OR Input');
    Memo1.Lines.Add('Neuron Value:');
  end;

  for n := 0 to jumlahdata-1 do
  begin
    //Second Layer
    for j := 0 to jumlahhiddenneuron1-1 do
    begin
      temporary := 0;
      for k := 0 to jumlahinputneuron-1 do
      begin
        temporary := temporary+inputlayer[k][n]*weight[0][k][j];
      end;
      temporary := temporary - tresholdlayer[1];
      hiddenlayer[0][j] := 1/(1+exp(-temporary));
    end;

    //Third Layer
    for j := 0 to jumlahhiddenneuron2-1 do
    begin
      temporary := 0;
      for k := 0 to jumlahhiddenneuron1-1 do
      begin
        temporary := temporary+hiddenlayer[0][k]*weight[1][k][j];
      end;
      temporary := temporary - tresholdlayer[2];
      hiddenlayer[1][j] := 1/(1+exp(-temporary));
    end;

    //Fourth Layer
    for j := 0 to jumlahoutputneuron-1 do
    begin
      temporary := 0;
      for k := 0 to jumlahhiddenneuron2-1 do
      begin
        temporary := temporary+hiddenlayer[1][k]*weight[2][k][j];
      end;
      temporary := temporary - tresholdlayer[3];
      hiddenlayer[2][j] := 1/(1+exp(-temporary));
      Memo1.Lines.Add('Layer Output Neuron ke '+inttostr(j)+'Sequence ke '+inttostr(n)+' = '+floattostr(hiddenlayer[2][j]));
    end;

    //Plot Output XOR
    if RadioButton1.Checked then
    begin
      if n = 0 then Series3.AddXY(n, hiddenlayer[2][0],'0',clRed);
      if n = 1 then Series3.AddXY(n, hiddenlayer[2][0],'1',clBlue);
      if n = 2 then Series3.AddXY(n, hiddenlayer[2][0],'1',clBlue);
      if n = 3 then Series3.AddXY(n, hiddenlayer[2][0],'0',clRed);
    end;

    //Plot Output Gait Phase
    if RadioButton2.Checked then
    begin
      Series4.AddXY(n, inputlayer[0][n], 'Input Layer 1' , clBlue);
      Series5.AddXY(n, inputlayer[1][n], 'Input Layer 2' , clRed);
      Series6.AddXY(n, hiddenlayer[2][0], 'Output Gait Phase', clGreen);
    end;

    //Plot Output AND
    if RadioButton3.Checked then
    begin
      if n = 0 then Series3.AddXY(n, hiddenlayer[2][0],'0',clRed);
      if n = 1 then Series3.AddXY(n, hiddenlayer[2][0],'0',clRed);
      if n = 2 then Series3.AddXY(n, hiddenlayer[2][0],'0',clRed);
      if n = 3 then Series3.AddXY(n, hiddenlayer[2][0],'1',clBlue);
    end;

    //Plot Output OR
    if RadioButton4.Checked then
    begin
      if n = 0 then Series3.AddXY(n, hiddenlayer[2][0],'0',clRed);
      if n = 1 then Series3.AddXY(n, hiddenlayer[2][0],'1',clBlue);
      if n = 2 then Series3.AddXY(n, hiddenlayer[2][0],'1',clBlue);
      if n = 3 then Series3.AddXY(n, hiddenlayer[2][0],'1',clBlue);
    end;

    if RadioButton5.Checked then
    begin
      Series4.AddXY(n, inputlayer[0][n], 'Input Layer 1' , clBlue);
      Series5.AddXY(n, inputlayer[1][n], 'Input Layer 2' , clRed);
      Series6.AddXY(n, hiddenlayer[2][0], 'Output Gait Phase 1', clGreen);
      Series7.AddXY(n, hiddenlayer[2][1], 'Output Gait Phase  2', clGreen);
      Series8.AddXY(n, hiddenlayer[2][2], 'Output Gait Phase 3', clGreen);
      Series9.AddXY(n, hiddenlayer[2][3], 'Output Gait Phase 4', clGreen);
      Series10.AddXY(n, hiddenlayer[2][4], 'Output Gait Phase 5', clGreen);
      Series11.AddXY(n, hiddenlayer[2][5], 'Output Gait Phase 6', clGreen);
    end;
  end;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  Application.Terminate;
end;


procedure TForm1.Button5Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        //Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else
      begin
        ReadLn(myFile, inputlayer[0][i-1]);
        Inc(i);
        //Memo1.Lines.Add(floattostr(inputlayer[0][i-1]));
      end;
    end;

    for n := 0 to jumlahdata do
    begin
      Series4.AddXY(n, inputlayer[0][n]);
    end;
    closefile(myFile);
    ShowMessage('File Import Complete');
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;
end;

procedure TForm1.Button6Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        //Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else
      begin
        ReadLn(myFile, inputlayer[1][i-1]);
        Inc(i);
        //Memo1.Lines.Add(floattostr(inputlayer[1][i-1]));
      end;
    end;

    for n := 0 to jumlahdata-1 do
    begin
      Series5.AddXY(n, inputlayer[1][n]);
    end;

    closefile(myFile);
    ShowMessage('File Import Complete');
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;
end;

procedure TForm1.Button7Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        //Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else
      begin
        ReadLn(myFile, outputlayer[0][i-1]);
        Inc(i);
        //Memo1.Lines.Add(floattostr(outputlayer[0][i-1]));
      end;
    end;

    for n := 0 to jumlahdata-1 do
    begin
      Series6.AddXY(n, outputlayer[0][n]);
    end;
    closefile(myFile);
    ShowMessage('File Import Complete');
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;
end;

procedure TForm1.Button8Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        //Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else
      begin
        ReadLn(myFile, outputlayer[1][i-1]);
        Inc(i);
        //Memo1.Lines.Add(floattostr(outputlayer[1][i-1]));
      end;
    end;

    for n := 0 to jumlahdata-1 do
    begin
      Series7.AddXY(n, outputlayer[1][n]);
    end;

    ShowMessage('File Import Complete');
    closefile(myFile);
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;
end;

procedure TForm1.Button9Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        //Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else
      begin
        ReadLn(myFile, outputlayer[2][i-1]);
        Inc(i);
        //Memo1.Lines.Add(floattostr(outputlayer[2][i-1]));
      end;
    end;

    for n := 0 to jumlahdata-1 do
    begin
      Series8.AddXY(n, outputlayer[2][n]);
    end;
    closefile(myFile);
    ShowMessage('File Import Complete');
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;

end;

procedure TForm1.Button10Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        //Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else
      begin
        ReadLn(myFile, outputlayer[3][i-1]);
        Inc(i);
        //Memo1.Lines.Add(floattostr(outputlayer[3][i-1]));
      end;
    end;

    for n := 0 to jumlahdata-1 do
    begin
      Series9.AddXY(n, outputlayer[3][n]);
    end;
    closefile(myFile);
    ShowMessage('File Import Complete');
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;

end;

procedure TForm1.Button11Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        //Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else
      begin
        ReadLn(myFile, outputlayer[4][i-1]);
        Inc(i);
        //Memo1.Lines.Add(floattostr(outputlayer[4][i-1]));
      end;
    end;

    for n := 0 to jumlahdata-1 do
    begin
      Series10.AddXY(n, outputlayer[4][n]);
    end;
    closefile(myFile);
    ShowMessage('File Import Complete');
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;
end;

procedure TForm1.Button12Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        //Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else
      begin
        ReadLn(myFile, outputlayer[5][i-1]);
        Inc(i);
        //Memo1.Lines.Add(floattostr(outputlayer[5][i-1]));
      end;
    end;

    for n := 0 to jumlahdata-1 do
    begin
      Series11.AddXY(n, outputlayer[5][n]);
    end;
    closefile(myFile);
    ShowMessage('File Import Complete');
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;
end;

procedure TForm1.Button13Click(Sender: TObject);
var
  i, n : Integer;
  myFile: TextFile;

begin
  openDialog1 := TOpenDialog.Create(self);
  openDialog1.InitialDir := GetCurrentDir;
  openDialog1.Options := [ofFileMustExist];
  openDialog1.Filter := 'Gait Phase Data|*.dat';
  if openDialog1.Execute then
  begin
    AssignFile(myFile, OpenDialog1.FileName);
    Reset(myFile);

    i := 0;
    while not EOF(myFile) do
    begin
      if i = 0 then
      begin
        ReadLn(myFile, jumlahdata);
        Memo1.Lines.Add(inttostr(jumlahdata));
        Inc(i);
      end else if i = 1 then
      begin
        ReadLn(myFile, jumlahoutputneuron);
        Memo1.Lines.Add(inttostr(jumlahoutputneuron));
        Inc(i);
      end else
      begin
        ReadLn(myFile, outputlayer[0][i-2], outputlayer[1][i-2], outputlayer[2][i-2], outputlayer[3][i-2], outputlayer[4][i-2], outputlayer[5][i-2]);
        Inc(i);
        Memo1.Lines.Add(floattostr(outputlayer[0][i-2])+' '+floattostr(outputlayer[1][i-2])+' '+floattostr(outputlayer[2][i-2])+' '+floattostr(outputlayer[3][i-2])+' '+floattostr(outputlayer[4][i-2])+' '+floattostr(outputlayer[5][i-2]));
      end;
    end;

    for n := 0 to jumlahdata-1 do
    begin
      Series6.AddXY(n, outputlayer[0][n]);
      Series7.AddXY(n, outputlayer[1][n]);
      Series8.AddXY(n, outputlayer[2][n]);
      Series9.AddXY(n, outputlayer[3][n]);
      Series10.AddXY(n, outputlayer[4][n]);
      Series11.AddXY(n, outputlayer[5][n]);
    end;
    closefile(myFile);
    edit4.Text := inttostr(jumlahoutputneuron);
    ShowMessage('File Import Complete');
  end else ShowMessage('Open file was cancelled');
  openDialog1.Free;
end;

procedure TForm1.Button16Click(Sender: TObject);
var
  i : Integer;
  myFile: TextFile;

begin
  jumlahoutputneuron:=strtoint(Edit4.text);
  AssignFile(myFile, 'Export 6 Output Data.dat');
  ReWrite(myFile);

  for i := 0 to jumlahdata+1 do
  begin
    if i = 0 then
    begin
      Write(myFile, jumlahdata);
      WriteLn(myFile);
    end else if i = 1 then
    begin
      Write(myFile, jumlahoutputneuron);
      WriteLn(myFile);
    end else
    begin
      Write(myFile,outputlayer[0][i-2]);
      Write(myFile,outputlayer[1][i-2]);
      Write(myFile,outputlayer[2][i-2]);
      Write(myFile,outputlayer[3][i-2]);
      Write(myFile,outputlayer[4][i-2]);
      Write(myFile,outputlayer[5][i-2]);
      WriteLn(myFile);
    end;
  end;

  closeFile(myFile);
  ShowMessage('File Export Complete');
end;


procedure TForm1.Button17Click(Sender: TObject);
begin
  Memo1.Clear;
  Series1.Clear;
  Series2.Clear;
  Series3.Clear;
  Series4.Clear;
  Series5.Clear;
  Series6.Clear;
  Series7.Clear;
  Series8.Clear;
  Series9.Clear;
  Series10.Clear;
  Series11.Clear;
end;

end.
