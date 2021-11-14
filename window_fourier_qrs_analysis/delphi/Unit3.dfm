object Form3: TForm3
  Left = 0
  Top = 0
  Caption = 'ONLINE'
  ClientHeight = 714
  ClientWidth = 927
  Color = clHighlightText
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object Label3: TLabel
    Left = 44
    Top = 72
    Width = 41
    Height = 13
    Caption = 'Iterasi : '
  end
  object Label2: TLabel
    Left = 818
    Top = 26
    Width = 61
    Height = 13
    Caption = 'HEART BEAT'
  end
  object Label1: TLabel
    Left = 38
    Top = 94
    Width = 89
    Height = 22
    Caption = 'THRESHOLD'
    Font.Charset = ANSI_CHARSET
    Font.Color = clWindowText
    Font.Height = -16
    Font.Name = 'Trebuchet MS'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object Chart1: TChart
    Left = 168
    Top = 8
    Width = 751
    Height = 169
    Legend.CheckBoxes = True
    MarginLeft = 1
    MarginRight = 6
    Title.Text.Strings = (
      'ECG SIGNAL')
    BottomAxis.Automatic = False
    BottomAxis.AutomaticMaximum = False
    BottomAxis.AutomaticMinimum = False
    BottomAxis.Grid.Visible = False
    BottomAxis.Maximum = 1800.000000000000000000
    BottomAxis.Title.Caption = 'Sequence[n]'
    LeftAxis.Automatic = False
    LeftAxis.AutomaticMaximum = False
    LeftAxis.AutomaticMinimum = False
    LeftAxis.Grid.Visible = False
    LeftAxis.Maximum = 1.000000000000000000
    LeftAxis.Minimum = -0.600000000000000000
    LeftAxis.Title.Caption = 'Amplitudo'
    View3D = False
    Color = clHighlightText
    TabOrder = 0
    DefaultCanvas = 'TGDIPlusCanvas'
    ColorPaletteIndex = 18
    object ECGOnline: TLineSeries
      SeriesColor = clBlack
      Title = 'ECG'
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
    object PeakOnline: TPointSeries
      Marks.Callout.Length = 8
      Title = 'Peak'
      ClickableLine = False
      Pointer.InflateMargins = True
      Pointer.Style = psCircle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
  end
  object Chart2: TChart
    Left = 168
    Top = 183
    Width = 751
    Height = 169
    Legend.CheckBoxes = True
    MarginRight = 2
    Title.Text.Strings = (
      'FILTERED ECG')
    BottomAxis.Automatic = False
    BottomAxis.AutomaticMaximum = False
    BottomAxis.AutomaticMinimum = False
    BottomAxis.Grid.Visible = False
    BottomAxis.Maximum = 1800.000000000000000000
    BottomAxis.Title.Caption = 'Sequence[n]'
    LeftAxis.Grid.Visible = False
    LeftAxis.Title.Caption = 'Amplitudo'
    View3D = False
    Color = clHighlightText
    TabOrder = 1
    DefaultCanvas = 'TGDIPlusCanvas'
    ColorPaletteIndex = 18
    object BPFonline: TLineSeries
      SeriesColor = clRed
      Title = 'BPF'
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
    object DerivativeOnline: TLineSeries
      SeriesColor = 65408
      Title = 'Derivative'
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
    object SquaringOnline: TLineSeries
      SeriesColor = 12615680
      Title = 'Squaring'
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
    object MAVOnline: TLineSeries
      SeriesColor = 4227327
      Title = 'MAV'
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
    object ThresholdOnline: TLineSeries
      SeriesColor = 8388863
      Title = 'Threshold'
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
    object LPOnline: TLineSeries
      SeriesColor = clOlive
      Title = 'LP'
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
    object LNOnline: TLineSeries
      SeriesColor = 7846911
      Title = 'LN'
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
  end
  object Chart3: TChart
    Left = 168
    Top = 358
    Width = 751
    Height = 169
    Legend.Visible = False
    MarginLeft = 4
    MarginRight = 18
    Title.Text.Strings = (
      'R BINER FROM THRESHOLDING')
    BottomAxis.Automatic = False
    BottomAxis.AutomaticMaximum = False
    BottomAxis.AutomaticMinimum = False
    BottomAxis.Maximum = 1800.000000000000000000
    LeftAxis.Automatic = False
    LeftAxis.AutomaticMaximum = False
    LeftAxis.AutomaticMinimum = False
    LeftAxis.Maximum = 1.200000000000000000
    LeftAxis.Minimum = -0.200000000000000000
    View3D = False
    Color = clHighlightText
    TabOrder = 2
    DefaultCanvas = 'TGDIPlusCanvas'
    ColorPaletteIndex = 18
    object BinerOnline: TLineSeries
      SeriesColor = clBlack
      Title = 'Biner'
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
  end
  object OnlineButton: TButton
    Left = 8
    Top = 13
    Width = 145
    Height = 49
    Caption = 'Online'
    TabOrder = 3
    OnClick = OnlineButtonClick
  end
  object ListBox1: TListBox
    Left = 8
    Top = 122
    Width = 145
    Height = 188
    ItemHeight = 13
    TabOrder = 4
  end
  object FFedit: TLabeledEdit
    Left = 8
    Top = 364
    Width = 121
    Height = 21
    EditLabel.Width = 84
    EditLabel.Height = 13
    EditLabel.Caption = 'Forgetting Factor'
    TabOrder = 5
    Text = '0.8'
  end
  object OrdeEdit: TLabeledEdit
    Left = 8
    Top = 412
    Width = 121
    Height = 21
    EditLabel.Width = 88
    EditLabel.Height = 13
    EditLabel.Caption = 'Orde of MAV Filter'
    TabOrder = 6
    Text = '35'
  end
  object ErrorEdit: TLabeledEdit
    Left = 8
    Top = 457
    Width = 121
    Height = 21
    EditLabel.Width = 61
    EditLabel.Height = 13
    EditLabel.Caption = 'Error Manual'
    TabOrder = 7
    Text = '35'
  end
  object GroupBox1: TGroupBox
    Left = 14
    Top = 534
    Width = 905
    Height = 172
    Caption = 'BPM Calculation'
    TabOrder = 8
    object Label4: TLabel
      Left = 24
      Top = 76
      Width = 36
      Height = 24
      Caption = 'BPM'
      Font.Charset = ANSI_CHARSET
      Font.Color = clWindowText
      Font.Height = -19
      Font.Name = 'Trebuchet MS'
      Font.Style = [fsBold]
      ParentFont = False
    end
    object Label5: TLabel
      Left = 161
      Top = 64
      Width = 65
      Height = 44
      Alignment = taCenter
      Caption = 'Iteration for R'
      Font.Charset = ANSI_CHARSET
      Font.Color = clWindowText
      Font.Height = -16
      Font.Name = 'Trebuchet MS'
      Font.Style = [fsBold]
      ParentFont = False
      WordWrap = True
    end
    object Label6: TLabel
      Left = 438
      Top = 64
      Width = 56
      Height = 44
      Alignment = taCenter
      Caption = 'R-to-R Interval'
      Font.Charset = ANSI_CHARSET
      Font.Color = clWindowText
      Font.Height = -16
      Font.Name = 'Trebuchet MS'
      Font.Style = [fsBold]
      ParentFont = False
      WordWrap = True
    end
    object Label7: TLabel
      Left = 705
      Top = 64
      Width = 45
      Height = 44
      Alignment = taCenter
      Caption = 'BPM Result'
      Font.Charset = ANSI_CHARSET
      Font.Color = clWindowText
      Font.Height = -16
      Font.Name = 'Trebuchet MS'
      Font.Style = [fsBold]
      ParentFont = False
      WordWrap = True
    end
    object ListBox2: TListBox
      Left = 232
      Top = 23
      Width = 127
      Height = 133
      ItemHeight = 13
      TabOrder = 0
    end
    object ListBox3: TListBox
      Left = 508
      Top = 23
      Width = 121
      Height = 133
      ItemHeight = 13
      TabOrder = 1
    end
    object ListBox4: TListBox
      Left = 768
      Top = 23
      Width = 121
      Height = 133
      ItemHeight = 13
      TabOrder = 2
    end
  end
end
