unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, dbf, FileUtil, Forms, Controls, Graphics, Dialogs,
  StdCtrls, ExtCtrls, Grids;

type

  { TForm1 }

  TForm1 = class(TForm)
    Perkalian: TButton;
    StringGrid3: TStringGrid;
    Tambah: TButton;
    Matriks: TButton;
    Kurang: TButton;
    Edit2: TEdit;
    Edit1: TEdit;
    Edit4: TEdit;
    Edit3: TEdit;
    StringGrid1: TStringGrid;
    StringGrid2: TStringGrid;
    procedure PerkalianClick(Sender: TObject);
    procedure KurangClick(Sender: TObject);
    procedure TambahClick(Sender: TObject);
    procedure MatriksClick(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  a, b, c, d, e, f: Integer;
  z, x, y: String;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.TambahClick(Sender: TObject);
begin
  If (StrToInt(Edit2.Text)=StrToInt(Edit4.Text)) AND (StrToInt(Edit1.Text)=StrToInt(Edit3.Text)) then
    begin
      StringGrid3.ColCount:=StrToInt(Edit2.Text)+1;
      StringGrid3.RowCount:=StrToInt(Edit1.Text)+1;
      For a:=1 to (StrToInt(Edit2.Text)) do
      begin
        For b:=1 to (StrToInt(Edit1.Text)) do
        begin
          z:=StringGrid1.Cells[a,b];
          x:=StringGrid2.Cells[a,b];
          c:=StrToInt(z)+StrToInt(x);
          StringGrid3.Cells[a,b]:=IntToStr(c);
        end;
      end;
    end
  else
  begin
    ShowMessage('Error, dimensi matriks A tidak sama dengan dimensi matriks B');
  end;
end;

procedure TForm1.KurangClick(Sender: TObject);
begin
  If (StrToInt(Edit2.Text)=StrToInt(Edit4.Text)) AND (StrToInt(Edit1.Text)=StrToInt(Edit3.Text)) then
    begin
      StringGrid3.ColCount:=StrToInt(Edit2.Text)+1;
      StringGrid3.RowCount:=StrToInt(Edit1.Text)+1;
      For a:=1 to (StrToInt(Edit2.Text)) do
      begin
        For b:=1 to (StrToInt(Edit1.Text)) do
        begin
          z:=StringGrid1.Cells[a,b];
          x:=StringGrid2.Cells[a,b];
          c:=StrToInt(z)-StrToInt(x);
          StringGrid3.Cells[a,b]:=IntToStr(c);
        end;
      end;
    end
  else
  begin
    ShowMessage('Error, dimensi matriks A tidak sama dengan dimensi matriks B');
  end;

end;

procedure TForm1.PerkalianClick(Sender: TObject);
begin
  If (StrToInt(Edit1.Text)=StrToInt(Edit4.Text)) then
    begin
      StringGrid3.ColCount:=StrToInt(Edit1.Text)+1;
      StringGrid3.RowCount:=StrToInt(Edit4.Text)+1;
      f:=0;
      For a:=1 to (StrToInt(Edit1.Text)) do
      begin
        For b:=1 to (StrToInt(Edit4.Text)) do
        begin
          For c:=1 to (StrToInt(Edit2.Text)) do
          begin
            z:=StringGrid1.Cells[a,c];
            x:=StringGrid2.Cells[c,b];
            f:=f+(StrToInt(x)*StrToInt(z));
          end;
          StringGrid3.Cells[b,a]:=IntToStr(f);
          f:=0;
        end;
      end;
    end
    else
    begin
      ShowMessage('Error, Kolom matriks A tidak sama dengan baris matriks B');
    end;

end;

procedure TForm1.MatriksClick(Sender: TObject);
begin
  StringGrid1.ColCount:=StrToInt(Edit1.Text)+1;
  StringGrid1.RowCount:=StrToInt(Edit2.Text)+1;

  StringGrid2.ColCount:=StrToInt(Edit3.Text)+1;
  StringGrid2.RowCount:=StrToInt(Edit4.Text)+1;

end;

end.

