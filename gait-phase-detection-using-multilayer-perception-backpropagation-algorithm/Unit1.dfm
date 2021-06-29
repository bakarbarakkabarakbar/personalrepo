object Form1: TForm1
  Left = 220
  Top = 183
  Width = 1097
  Height = 472
  Caption = 'Form1'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object Label5: TLabel
    Left = 592
    Top = 152
    Width = 46
    Height = 13
    Caption = 'Error Limit'
  end
  object Label6: TLabel
    Left = 440
    Top = 152
    Width = 52
    Height = 13
    Caption = 'Iterasi Limit'
  end
  object GroupBox4: TGroupBox
    Left = 224
    Top = 0
    Width = 185
    Height = 65
    Caption = 'Layer Selection'
    TabOrder = 30
    object Label1: TLabel
      Left = 8
      Top = 16
      Width = 24
      Height = 13
      Caption = 'Input'
    end
    object Label2: TLabel
      Left = 8
      Top = 40
      Width = 43
      Height = 13
      Caption = 'Hidden 1'
    end
    object Label3: TLabel
      Left = 104
      Top = 16
      Width = 43
      Height = 13
      Caption = 'Hidden 2'
    end
    object Label4: TLabel
      Left = 104
      Top = 40
      Width = 32
      Height = 13
      Caption = 'Output'
    end
  end
  object GroupBox3: TGroupBox
    Left = 16
    Top = 72
    Width = 81
    Height = 73
    Caption = 'Input Data'
    TabOrder = 29
  end
  object GroupBox1: TGroupBox
    Left = 96
    Top = 72
    Width = 225
    Height = 97
    Caption = '6 Output Neuron'
    TabOrder = 28
  end
  object Button1: TButton
    Left = 432
    Top = 16
    Width = 105
    Height = 25
    Caption = '1. Random Weight'
    TabOrder = 0
    OnClick = Button1Click
  end
  object RadioGroup1: TRadioGroup
    Left = 16
    Top = 0
    Width = 209
    Height = 65
    Caption = 'Neural Network Selection'
    TabOrder = 1
  end
  object RadioButton1: TRadioButton
    Left = 24
    Top = 16
    Width = 113
    Height = 17
    Caption = 'XOR'
    TabOrder = 2
    OnClick = RadioButton1Click
  end
  object Memo1: TMemo
    Left = 544
    Top = 8
    Width = 529
    Height = 137
    Lines.Strings = (
      'Me'
      'mo'
      '1')
    ScrollBars = ssVertical
    TabOrder = 3
  end
  object Edit1: TEdit
    Left = 288
    Top = 16
    Width = 25
    Height = 21
    TabOrder = 4
    Text = '2'
  end
  object Edit2: TEdit
    Left = 288
    Top = 40
    Width = 25
    Height = 21
    TabOrder = 5
    Text = '8'
  end
  object Edit3: TEdit
    Left = 376
    Top = 16
    Width = 25
    Height = 21
    TabOrder = 6
    Text = '8'
  end
  object Edit4: TEdit
    Left = 376
    Top = 40
    Width = 25
    Height = 21
    TabOrder = 7
    Text = '6'
  end
  object RadioButton2: TRadioButton
    Left = 80
    Top = 16
    Width = 113
    Height = 17
    Caption = 'Gait Phase'
    TabOrder = 8
    OnClick = RadioButton2Click
  end
  object Chart1: TChart
    Left = 24
    Top = 176
    Width = 129
    Height = 121
    BackWall.Brush.Color = clWhite
    BackWall.Brush.Style = bsClear
    Title.Text.Strings = (
      'Error Sequence')
    Legend.Visible = False
    View3D = False
    TabOrder = 9
    object Series1: TFastLineSeries
      Marks.ArrowLength = 8
      Marks.Visible = False
      SeriesColor = clRed
      LinePen.Color = clRed
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
  end
  object Chart2: TChart
    Left = 432
    Top = 176
    Width = 633
    Height = 249
    BackWall.Brush.Color = clWhite
    BackWall.Brush.Style = bsClear
    Title.Text.Strings = (
      'Gait Phase')
    Legend.Alignment = laBottom
    Legend.ColorWidth = 10
    Legend.ShadowSize = 0
    View3D = False
    TabOrder = 10
    object Series4: TFastLineSeries
      Marks.ArrowLength = 8
      Marks.Visible = False
      PercentFormat = '##0,## %'
      SeriesColor = clRed
      Title = 'Input 1'
      ValueFormat = '#,##0,###'
      LinePen.Color = clRed
      LinePen.Width = 2
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
    object Series5: TFastLineSeries
      Marks.ArrowLength = 8
      Marks.Visible = False
      SeriesColor = clGreen
      Title = 'Input 2'
      LinePen.Color = clGreen
      LinePen.Width = 2
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
    object Series6: TFastLineSeries
      Marks.ArrowLength = 8
      Marks.Visible = False
      SeriesColor = clYellow
      Title = 'Output 1'
      LinePen.Color = clYellow
      LinePen.Width = 2
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
    object Series7: TFastLineSeries
      Marks.ArrowLength = 8
      Marks.Visible = False
      SeriesColor = clBlue
      Title = 'Output 2'
      LinePen.Color = clBlue
      LinePen.Width = 2
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
    object Series8: TFastLineSeries
      Marks.ArrowLength = 8
      Marks.Visible = False
      SeriesColor = 4194368
      Title = 'Output 3'
      LinePen.Color = 4194368
      LinePen.Width = 2
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
    object Series9: TFastLineSeries
      Marks.ArrowLength = 8
      Marks.Visible = False
      SeriesColor = clGray
      Title = 'Output 4'
      LinePen.Color = clGray
      LinePen.Width = 2
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
    object Series10: TFastLineSeries
      Marks.ArrowLength = 8
      Marks.Visible = False
      SeriesColor = clFuchsia
      Title = 'Output 5'
      LinePen.Color = clFuchsia
      LinePen.Width = 2
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
    object Series11: TFastLineSeries
      Marks.ArrowLength = 8
      Marks.Visible = False
      SeriesColor = clTeal
      Title = 'Output 6'
      LinePen.Color = clTeal
      LinePen.Width = 2
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
  end
  object Chart3: TChart
    Left = 24
    Top = 296
    Width = 129
    Height = 129
    BackWall.Brush.Color = clWhite
    BackWall.Brush.Style = bsClear
    Title.Text.Strings = (
      'Input Data')
    Legend.Visible = False
    View3D = False
    TabOrder = 11
    object Series2: TPointSeries
      Marks.ArrowLength = 0
      Marks.Visible = False
      SeriesColor = clGreen
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      Pointer.Visible = True
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Y'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
  end
  object Chart4: TChart
    Left = 160
    Top = 176
    Width = 265
    Height = 249
    BackWall.Brush.Color = clWhite
    BackWall.Brush.Style = bsClear
    Title.Text.Strings = (
      'Output Data')
    Legend.Visible = False
    View3D = False
    TabOrder = 12
    object Series3: TBarSeries
      Marks.ArrowLength = 20
      Marks.Visible = True
      SeriesColor = clRed
      XValues.DateTime = False
      XValues.Name = 'X'
      XValues.Multiplier = 1.000000000000000000
      XValues.Order = loAscending
      YValues.DateTime = False
      YValues.Name = 'Bar'
      YValues.Multiplier = 1.000000000000000000
      YValues.Order = loNone
    end
  end
  object Button2: TButton
    Left = 448
    Top = 40
    Width = 73
    Height = 25
    Caption = '2. Learning'
    TabOrder = 13
    OnClick = Button2Click
  end
  object Button3: TButton
    Left = 448
    Top = 64
    Width = 73
    Height = 25
    Caption = '3. Open Data'
    TabOrder = 14
    OnClick = Button3Click
  end
  object Button4: TButton
    Left = 456
    Top = 112
    Width = 57
    Height = 25
    Caption = '5. Close'
    TabOrder = 15
    OnClick = Button4Click
  end
  object RadioButton3: TRadioButton
    Left = 24
    Top = 40
    Width = 113
    Height = 17
    Caption = 'AND'
    TabOrder = 16
    OnClick = RadioButton3Click
  end
  object RadioButton4: TRadioButton
    Left = 168
    Top = 16
    Width = 49
    Height = 17
    Caption = 'OR'
    TabOrder = 17
    OnClick = RadioButton4Click
  end
  object Button5: TButton
    Left = 24
    Top = 88
    Width = 65
    Height = 25
    Caption = 'Input Data1'
    TabOrder = 18
    OnClick = Button5Click
  end
  object Button6: TButton
    Left = 24
    Top = 112
    Width = 65
    Height = 25
    Caption = 'Input Data2'
    TabOrder = 19
    OnClick = Button6Click
  end
  object Button7: TButton
    Left = 104
    Top = 88
    Width = 75
    Height = 25
    Caption = 'Target Output1'
    TabOrder = 20
    OnClick = Button7Click
  end
  object RadioButton5: TRadioButton
    Left = 80
    Top = 40
    Width = 113
    Height = 17
    Caption = 'Manual Input Data'
    TabOrder = 21
    OnClick = RadioButton5Click
  end
  object Button8: TButton
    Left = 104
    Top = 112
    Width = 75
    Height = 25
    Caption = 'Target Output2'
    TabOrder = 22
    OnClick = Button8Click
  end
  object Button9: TButton
    Left = 104
    Top = 136
    Width = 75
    Height = 25
    Caption = 'Target Output3'
    TabOrder = 23
    OnClick = Button9Click
  end
  object Button10: TButton
    Left = 184
    Top = 88
    Width = 75
    Height = 25
    Caption = 'Target Output4'
    TabOrder = 24
    OnClick = Button10Click
  end
  object Button11: TButton
    Left = 184
    Top = 112
    Width = 75
    Height = 25
    Caption = 'Target Output5'
    TabOrder = 25
    OnClick = Button11Click
  end
  object Button12: TButton
    Left = 184
    Top = 136
    Width = 75
    Height = 25
    Caption = 'Target Output6'
    TabOrder = 26
    OnClick = Button12Click
  end
  object Button13: TButton
    Left = 264
    Top = 88
    Width = 49
    Height = 73
    Caption = 'Single File Target Output'
    TabOrder = 27
    WordWrap = True
    OnClick = Button13Click
  end
  object GroupBox5: TGroupBox
    Left = 320
    Top = 72
    Width = 113
    Height = 97
    Caption = 'Import Export'
    TabOrder = 31
    object Button14: TButton
      Left = 8
      Top = 16
      Width = 75
      Height = 25
      Caption = 'Import Weight'
      TabOrder = 0
    end
    object Button15: TButton
      Left = 8
      Top = 40
      Width = 75
      Height = 25
      Caption = 'Export Weight'
      TabOrder = 1
    end
    object Button16: TButton
      Left = 8
      Top = 64
      Width = 97
      Height = 25
      Caption = 'Export Output As 1'
      TabOrder = 2
      OnClick = Button16Click
    end
  end
  object Button17: TButton
    Left = 456
    Top = 88
    Width = 57
    Height = 25
    Caption = '4. Clear'
    TabOrder = 32
    OnClick = Button17Click
  end
  object Edit5: TEdit
    Left = 648
    Top = 152
    Width = 57
    Height = 21
    TabOrder = 33
    Text = '0.3'
  end
  object Edit6: TEdit
    Left = 504
    Top = 152
    Width = 81
    Height = 21
    TabOrder = 34
    Text = '20000'
  end
  object OpenDialog1: TOpenDialog
    Left = 1048
    Top = 8
  end
  object OpenDialog2: TOpenDialog
    Left = 1016
    Top = 8
  end
end
