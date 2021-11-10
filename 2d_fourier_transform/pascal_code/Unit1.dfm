object Form1: TForm1
  Left = 323
  Top = 100
  Width = 653
  Height = 387
  Caption = 'Form1'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Image1: TImage
    Left = 24
    Top = 40
    Width = 300
    Height = 300
    Center = True
    Stretch = True
  end
  object Image2: TImage
    Left = 328
    Top = 40
    Width = 300
    Height = 300
  end
  object Button1: TButton
    Left = 56
    Top = 8
    Width = 75
    Height = 25
    Caption = 'Open File'
    TabOrder = 0
    OnClick = Button1Click
  end
  object Button2: TButton
    Left = 136
    Top = 8
    Width = 75
    Height = 25
    Caption = 'GreyScale'
    TabOrder = 1
    OnClick = Button2Click
  end
  object Button4: TButton
    Left = 296
    Top = 8
    Width = 75
    Height = 25
    Caption = 'Close'
    TabOrder = 2
    OnClick = Button4Click
  end
  object Button3: TButton
    Left = 216
    Top = 8
    Width = 75
    Height = 25
    Caption = 'FFT2D'
    TabOrder = 3
    OnClick = Button3Click
  end
  object OpenDialog1: TOpenDialog
    Left = 328
    Top = 320
  end
end
