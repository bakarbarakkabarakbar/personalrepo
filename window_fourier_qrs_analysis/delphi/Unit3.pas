unit Unit3;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, VclTee.TeeGDIPlus, Vcl.StdCtrls,
  VCLTee.TeEngine, VCLTee.Series, Vcl.ExtCtrls, VCLTee.TeeProcs, math, dspinterface,
  VCLTee.Chart;

type
  arraybaru = array[-9999..9999] of real;
  TForm3 = class(TForm)
    Chart1: TChart;
    ECGOnline: TLineSeries;
    Chart2: TChart;
    BPFonline: TLineSeries;
    DerivativeOnline: TLineSeries;
    Chart3: TChart;
    BinerOnline: TLineSeries;
    OnlineButton: TButton;
    ListBox1: TListBox;
    SquaringOnline: TLineSeries;
    MAVOnline: TLineSeries;
    ThresholdOnline: TLineSeries;
    LPOnline: TLineSeries;
    LNOnline: TLineSeries;
    Label3: TLabel;
    PeakOnline: TPointSeries;
    Label2: TLabel;
    FFedit: TLabeledEdit;
    OrdeEdit: TLabeledEdit;
    ErrorEdit: TLabeledEdit;
    Label1: TLabel;
    GroupBox1: TGroupBox;
    ListBox2: TListBox;
    Label4: TLabel;
    ListBox3: TListBox;
    ListBox4: TListBox;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    procedure OnlineButtonClick(Sender: TObject);
    procedure delay(lama:longint);
    procedure FormCreate(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form3: TForm3;
  i,j,k : integer;
  yy, xx, ybackward, yforward : arraybaru;
  rr, tetaa : extended;
  bpm1, bpm2, bpm3, outp, interval : arraybaru;
  lp, ln, th : vektor;

implementation

{$R *.dfm}

uses Unit1, Unit2;

procedure TForm3.delay(lama:longint);
var
  ref : longint;
begin
  ref:=gettickcount;
  repeat application.processmessages;
  until ((gettickcount-ref)>=lama);
end;

procedure TForm3.FormCreate(Sender: TObject);
begin
 // heartbeatedit.Visible := False;
 // Listbox2.Visible := false;
 // label2.Visible := false;
end;

procedure TForm3.OnlineButtonClick(Sender: TObject);
var
  error : integer;
  temp, rpeak : extended;
  LN_Q, LP_Q, th_Q, v_Q, vQ_detek : vektor;
  max_q, tau_q, an_q, ap_q : extended;

begin
  ecgonline.Clear;
  peakonline.Clear;
  bpfonline.Clear;
  derivativeonline.Clear;
  squaringonline.Clear;
  MAVonline.Clear;
  ThresholdOnline.Clear;
  LPOnline.Clear;
  LNOnline.Clear;
  BinerOnline.Clear;
  Listbox1.Clear;
  ListBox2.Clear;
  listbox3.Clear;
  listbox4.Clear;
  label4.Caption := 'BPM';

  for i := 0 to 5000 do
  begin
    form1.outsqr[i] := 0;
    form1.outddt[i]:= 0;

    yforward[i]:= 0;
    ybackward[i]:= 0;
    outp[i]:= 0;
    bpm1[i]:= 0;
    bpm2[i] := 0;
    bpm3[i] := 0;
    interval[i] := 0;
  end;

  for i := 0 downto -5000 do
  begin
    form1.outsqr[i]:= 0;
    form1.outddt[i]:= 0;

    yforward[i]:= 0;
    ybackward[i]:= 0;
    outp[i]:= 0;

    bpm1[i]:= 0;
    bpm2[i] := 0;
    bpm3[i] := 0;
    interval[i] := 0;
  end;

  error := strtoint(erroredit.Text);
  max_Q :=0;

  for i := 0 to form1.jmldataecg-1 do
    begin
    v_Q[i]:= 0;
    LN_Q[i]:=0;
    LP_Q[i]:=0;
    end;

    tau_Q := strtofloat(ffedit.Text);
    AN_Q := 0.098;
    AP_Q := 0.098;


   listbox1.Items.Add('  Threshold  ');
   listbox2.Items.Add('----ITERASI R----');
   listbox3.Items.Add('----R R Interval----');
   listbox4.Items.Add('----BPM----');
   //listbox3.items.Add('Interval = ' + '-');
   //listbox4.items.Add('BPM = ' + '-');
   if onlinebutton.Caption='Online' then begin
    onlinebutton.Caption:='Stop';
    i:= 0;
    k:= 0;
    repeat
     label3.Caption:= 'Iterasi : '+ inttostr(i);
     ecgonline.AddXY(i, form1.xecgfilter[i]);
     bpfonline.AddXY(i, form2.y[i]);
     form1.outddt[i]:= ((2*form2.y[i]) + form2.y[i-1]- form2.y[i-3]-(2*form2.y[i-4]))/8;
     derivativeonline.AddXY(i, form1.outddt[i]);
     form1.outsqr[i]:= sqr(form1.outddt[i]);
     squaringonline.AddXY(i, form1.outsqr[i]);

     ordemav:=strtoint(OrdeEdit.Text);

     temp:= 0;
     j:= 0;
       repeat
          temp:= temp + form1.outsqr[i-j];
          inc(j)
       until (j= ordemav-1);
     ybackward[i]:= (1/ordemav)*temp;
     temp:= 0;
     j:= 0;
       repeat
         temp:= temp + ybackward[i+j];
         inc(j);
       until (j= ordemav-1);
     yforward[i]:= (1/ordemav)*temp;
     mavonline.AddXY(i, yforward[i]);

     //if yforward[i]> max_Q then max_Q := yforward[i]; //Max Level Peak

     if yforward[i]>v_Q[i-1] then v_Q[i]:=yforward[i]
     else
     begin
        v_Q[i]:=v_Q[i-1];
        if yforward[i]<=v_Q[i-1]/2 then v_Q[i]:=yforward[i];
     end;
     th_Q[i] := LN_Q[i-1] + tau_Q*abs(LP_Q[i-1]-LN_Q[i-1]);
     thresholdonline.AddXY(i ,th_q[i]);

     if v_Q[i] > th_Q[i] then  //LP
     begin
      LP_Q[i] := ((1-AP_q)*v_Q[i])+(AP_Q*LP_Q[i-1]);
     end
     else                      //LN
     begin
      LN_Q[i] := ((1-AN_Q)*v_Q[i])+(AN_Q*LN_Q[i-1]);
     end;
     lponline.AddXY(i ,LP_Q[i]);
     lnonline.AddXY(i, LN_Q[i]);

      listbox1.Items.Add('th['+inttostr(i)+']='+floattostr(th_q[i]));

      if yforward[i] > th_q[i] then
      begin
      outp[i]:= 1;
      inc(k);
      end
      else outp[i]:= 0;
      if (outp[i-1]=1) AND (outp[i] = 0) then
      begin
        peakonline.AddXY(i-error,form1.xecgfilter[i-error]);
      end;
      bineronline.AddXY(i,outp[i]);

      k:=0;
        if (outp[i]=0) and (outp[i-1]=1) then begin
            bpm1[k]:=i;
            listbox2.items.Add('Iterasi ke ' +floattostr(bpm1[k]));
            //if bpm3[k] <> bpm3[k-1] then
            //begin
              if interval[k] = 0 then
              begin
                listbox3.Items.Add('Interval = ' + '-');
              end else listbox3.Items.Add('Interval = ' + floattostr(interval[k]));

              if bpm3[k] = 0 then
              begin
                listbox4.Items.Add('BPM = ' + '-');
              end else listbox4.Items.Add('BPM = ' + floattostr(bpm3[k]));
            //end;

            //listbox4.Items.Add('BPM = ' + floattostr(bpm3[k]));
            inc(k);
            j:=i+1;
              repeat
                if (outp[j]=0) and (outp[j-1]=1) then begin
                  bpm2[k] := j;
                end;
                j := j-1;
              until (j = i-350);
        end;

      j:=0;

      if (i>220) then begin
        interval[j] := bpm1[j] - bpm2[j+1];
        bpm3[j]:=60/((interval[j])/form1.fsecg);
        bpm := bpm3[j];
        inc(j);
      end;

      if interval[k] = 0 then label4.Caption := 'BPM = ' + '-'
      else label4.Caption:= 'BPM = ' +floattostrF(bpm,ffFixed, 16, 2);

      i:=i+1;
      delay(1);
    until (onlinebutton.Caption='Online') or (i=form1.jmldataecg-1);
   end

    else if onlinebutton.Caption='Stop' then
    begin
    Listbox1.Clear;
    ListBox2.Clear;
    listbox3.Clear;
    listbox4.Clear;
    label4.Caption := 'BPM';
    onlinebutton.Caption:='Online';
   end;
end;

end.
