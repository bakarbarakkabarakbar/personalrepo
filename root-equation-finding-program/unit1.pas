unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, StdCtrls, Math;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Label1: TLabel;
    Label10: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    Label8: TLabel;
    Label9: TLabel;
    ListBox1: TListBox;
    ListBox2: TListBox;
    ListBox3: TListBox;
    ListBox4: TListBox;
    ListBox5: TListBox;
    ListBox6: TListBox;
    ListBox7: TListBox;
    procedure Button1Click(Sender: TObject);
  end;

var
  Form1 : TForm1;
  fc : Extended;
  xi, xu, xr, xerror : Extended;

implementation
{$R *.lfm}

function fungsi(c : Extended) : Extended;
begin
     fc := (667.38/c*(1-2.71828182846**(-0.147*c)))-40;
     result := fc;
end;

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
     ListBox1.clear;
     ListBox2.clear;
     ListBox3.clear;
     ListBox4.clear;
     ListBox5.clear;
     ListBox6.clear;
     ListBox7.clear;
     xi:=strtofloat(Edit1.Text);
     xu:=strtofloat(Edit2.Text);
     xerror:=strtofloat(Edit3.Text);
     repeat
        xr:=((xi*fungsi(xu))-(xu*fungsi(xi)))/(fungsi(xu)-fungsi(xi));
        ListBox1.Items.add(FloatToStr(xi));
        ListBox2.Items.add(FloatToStr(xu));
        ListBox3.Items.add(FloatToStr(xr));
        ListBox4.Items.add(FloatToStrF(fungsi(xi),ffnumber,12,12));
        ListBox5.Items.add(FloatToStrF(fungsi(xu),ffnumber,12,12));
        ListBox6.Items.add(FloatToStrF(fungsi(xr),ffnumber,12,12));
        ListBox7.Items.add(FloatToStrF((fungsi(xu)-fungsi(xi)),ffnumber,12,12));
        if (fungsi(xr)*fungsi(xi)<0) then
           xu:=xr;
        if (fungsi(xr)*fungsi(xi)>0) then
           xi:=xr;
     until (xu-xi)<xerror;
end;

end.

