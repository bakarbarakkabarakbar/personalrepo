object Form2: TForm2
  Left = 0
  Top = 0
  Caption = 'Form2'
  ClientHeight = 564
  ClientWidth = 802
  Color = clHighlightText
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 72
    Top = 280
    Width = 22
    Height = 13
    Caption = 'Teta'
  end
  object Label2: TLabel
    Left = 72
    Top = 239
    Width = 7
    Height = 13
    Caption = 'R'
  end
  object Label3: TLabel
    Left = 288
    Top = 8
    Width = 244
    Height = 31
    Caption = 'FILTER COMPARISON'
    Font.Charset = ANSI_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Trajan Pro 3'
    Font.Style = []
    ParentFont = False
  end
  object Button1: TButton
    Left = 8
    Top = 343
    Width = 81
    Height = 41
    Caption = 'Pantomkins'
    TabOrder = 0
    OnClick = Button1Click
  end
  object Chart1: TChart
    Left = 193
    Top = 48
    Width = 602
    Height = 161
    Legend.Font.Color = 4210752
    Legend.Font.Height = -13
    Legend.Font.Name = 'Verdana'
    Legend.Frame.Visible = False
    Legend.Transparent = True
    Legend.Visible = False
    Title.Font.Color = clGray
    Title.Font.Height = -16
    Title.Text.Strings = (
      'FILTER PANTOMKINS')
    BottomAxis.Grid.Visible = False
    BottomAxis.LabelsFormat.Font.Color = clGray
    BottomAxis.LabelsFormat.Font.Height = -13
    BottomAxis.LabelsFormat.Font.Name = 'Verdana'
    BottomAxis.MinorTicks.Visible = False
    BottomAxis.Title.Font.Color = 4210752
    BottomAxis.Title.Font.Height = -15
    DepthAxis.LabelsFormat.Font.Color = clGray
    DepthAxis.LabelsFormat.Font.Height = -13
    DepthAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthAxis.MinorTicks.Visible = False
    DepthAxis.Title.Font.Color = 4210752
    DepthAxis.Title.Font.Height = -15
    DepthTopAxis.LabelsFormat.Font.Color = clGray
    DepthTopAxis.LabelsFormat.Font.Height = -13
    DepthTopAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthTopAxis.MinorTicks.Visible = False
    DepthTopAxis.Title.Font.Color = 4210752
    DepthTopAxis.Title.Font.Height = -15
    LeftAxis.Axis.Visible = False
    LeftAxis.LabelsFormat.Font.Color = clGray
    LeftAxis.LabelsFormat.Font.Height = -13
    LeftAxis.LabelsFormat.Font.Name = 'Verdana'
    LeftAxis.MinorTicks.Visible = False
    LeftAxis.Title.Font.Color = 4210752
    LeftAxis.Title.Font.Height = -15
    RightAxis.LabelsFormat.Font.Color = clGray
    RightAxis.LabelsFormat.Font.Height = -13
    RightAxis.LabelsFormat.Font.Name = 'Verdana'
    RightAxis.MinorTicks.Visible = False
    RightAxis.Title.Font.Color = 4210752
    RightAxis.Title.Font.Height = -15
    TopAxis.LabelsFormat.Font.Color = clGray
    TopAxis.LabelsFormat.Font.Height = -13
    TopAxis.LabelsFormat.Font.Name = 'Verdana'
    TopAxis.MinorTicks.Visible = False
    TopAxis.Title.Font.Color = 4210752
    TopAxis.Title.Font.Height = -15
    View3D = False
    View3DWalls = False
    Color = clWhite
    TabOrder = 1
    DefaultCanvas = 'TGDIPlusCanvas'
    ColorPaletteIndex = -2
    ColorPalette = (
      14063991
      6868991
      4685823
      14404225
      10384222
      9875024
      4275174
      9499647
      13757072
      10724259
      12648447
      15198183)
    object Series1: TLineSeries
      Marks.Brush.Color = 6868991
      Marks.Font.Name = 'Verdana'
      Marks.RoundSize = 0
      Marks.Shadow.Visible = False
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
  end
  object Chart2: TChart
    Left = 193
    Top = 223
    Width = 602
    Height = 162
    Legend.Font.Color = 4210752
    Legend.Font.Height = -13
    Legend.Font.Name = 'Verdana'
    Legend.Frame.Visible = False
    Legend.Transparent = True
    Legend.Visible = False
    Title.Font.Color = clGray
    Title.Font.Height = -16
    Title.Text.Strings = (
      'FILTER BPF POLE ZERO')
    BottomAxis.Grid.Visible = False
    BottomAxis.LabelsFormat.Font.Color = clGray
    BottomAxis.LabelsFormat.Font.Height = -13
    BottomAxis.LabelsFormat.Font.Name = 'Verdana'
    BottomAxis.MinorTicks.Visible = False
    BottomAxis.Title.Font.Color = 4210752
    BottomAxis.Title.Font.Height = -15
    DepthAxis.LabelsFormat.Font.Color = clGray
    DepthAxis.LabelsFormat.Font.Height = -13
    DepthAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthAxis.MinorTicks.Visible = False
    DepthAxis.Title.Font.Color = 4210752
    DepthAxis.Title.Font.Height = -15
    DepthTopAxis.LabelsFormat.Font.Color = clGray
    DepthTopAxis.LabelsFormat.Font.Height = -13
    DepthTopAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthTopAxis.MinorTicks.Visible = False
    DepthTopAxis.Title.Font.Color = 4210752
    DepthTopAxis.Title.Font.Height = -15
    LeftAxis.Axis.Visible = False
    LeftAxis.LabelsFormat.Font.Color = clGray
    LeftAxis.LabelsFormat.Font.Height = -13
    LeftAxis.LabelsFormat.Font.Name = 'Verdana'
    LeftAxis.MinorTicks.Visible = False
    LeftAxis.Title.Font.Color = 4210752
    LeftAxis.Title.Font.Height = -15
    RightAxis.LabelsFormat.Font.Color = clGray
    RightAxis.LabelsFormat.Font.Height = -13
    RightAxis.LabelsFormat.Font.Name = 'Verdana'
    RightAxis.MinorTicks.Visible = False
    RightAxis.Title.Font.Color = 4210752
    RightAxis.Title.Font.Height = -15
    TopAxis.LabelsFormat.Font.Color = clGray
    TopAxis.LabelsFormat.Font.Height = -13
    TopAxis.LabelsFormat.Font.Name = 'Verdana'
    TopAxis.MinorTicks.Visible = False
    TopAxis.Title.Font.Color = 4210752
    TopAxis.Title.Font.Height = -15
    View3D = False
    View3DWalls = False
    Color = clWhite
    TabOrder = 2
    DefaultCanvas = 'TGDIPlusCanvas'
    ColorPaletteIndex = -2
    ColorPalette = (
      14063991
      6868991
      4685823
      14404225
      10384222
      9875024
      4275174
      9499647
      13757072
      10724259
      12648447
      15198183)
    object Series2: TLineSeries
      Marks.Brush.Color = 6868991
      Marks.Font.Name = 'Verdana'
      Marks.RoundSize = 0
      Marks.Shadow.Visible = False
      Brush.BackColor = clDefault
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
  end
  object Button2: TButton
    Left = 104
    Top = 343
    Width = 83
    Height = 42
    Caption = 'Pole Zero'
    TabOrder = 3
    OnClick = Button2Click
  end
  object Chart3: TChart
    Left = 8
    Top = 46
    Width = 179
    Height = 187
    BackWall.Brush.Gradient.Direction = gdBottomTop
    BackWall.Brush.Gradient.EndColor = clWhite
    BackWall.Brush.Gradient.StartColor = 15395562
    BackWall.Brush.Gradient.Visible = True
    BackWall.Transparent = False
    Foot.Font.Color = clBlue
    Foot.Font.Name = 'Verdana'
    Gradient.Direction = gdBottomTop
    Gradient.EndColor = clWhite
    Gradient.MidColor = 15395562
    Gradient.StartColor = 15395562
    Gradient.Visible = True
    LeftWall.Color = 14745599
    Legend.Font.Name = 'Verdana'
    Legend.Shadow.Transparency = 0
    Legend.Visible = False
    MarginBottom = 3
    MarginLeft = 0
    MarginRight = 6
    MarginTop = 16
    RightWall.Color = 14745599
    Title.Font.Name = 'Verdana'
    Title.Text.Strings = (
      'TChart')
    Title.Visible = False
    BottomAxis.Automatic = False
    BottomAxis.AutomaticMaximum = False
    BottomAxis.AutomaticMinimum = False
    BottomAxis.Axis.Color = 4210752
    BottomAxis.Grid.Color = 11119017
    BottomAxis.Grid.Visible = False
    BottomAxis.LabelsFormat.Font.Name = 'Verdana'
    BottomAxis.Maximum = 1.000000000000000000
    BottomAxis.Minimum = -1.000000000000000000
    BottomAxis.TicksInner.Color = 11119017
    BottomAxis.Title.Font.Name = 'Verdana'
    DepthAxis.Axis.Color = 4210752
    DepthAxis.Grid.Color = 11119017
    DepthAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthAxis.TicksInner.Color = 11119017
    DepthAxis.Title.Font.Name = 'Verdana'
    DepthTopAxis.Axis.Color = 4210752
    DepthTopAxis.Grid.Color = 11119017
    DepthTopAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthTopAxis.TicksInner.Color = 11119017
    DepthTopAxis.Title.Font.Name = 'Verdana'
    LeftAxis.Automatic = False
    LeftAxis.AutomaticMaximum = False
    LeftAxis.AutomaticMinimum = False
    LeftAxis.Axis.Color = 4210752
    LeftAxis.Grid.Color = 11119017
    LeftAxis.Grid.Visible = False
    LeftAxis.LabelsFormat.Font.Name = 'Verdana'
    LeftAxis.Maximum = 1.000000000000000000
    LeftAxis.Minimum = -1.000000000000000000
    LeftAxis.TicksInner.Color = 11119017
    LeftAxis.Title.Font.Name = 'Verdana'
    RightAxis.Axis.Color = 4210752
    RightAxis.Grid.Color = 11119017
    RightAxis.LabelsFormat.Font.Name = 'Verdana'
    RightAxis.TicksInner.Color = 11119017
    RightAxis.Title.Font.Name = 'Verdana'
    TopAxis.Axis.Color = 4210752
    TopAxis.Grid.Color = 11119017
    TopAxis.LabelsFormat.Font.Name = 'Verdana'
    TopAxis.TicksInner.Color = 11119017
    TopAxis.Title.Font.Name = 'Verdana'
    View3D = False
    ParentColor = True
    TabOrder = 4
    DefaultCanvas = 'TGDIPlusCanvas'
    ColorPaletteIndex = 13
    object LineSeries1: TLineSeries
      SeriesColor = clWindow
      Brush.BackColor = clDefault
      OutLine.Color = clNone
      OutLine.Style = psClear
      Pointer.HorizSize = 1
      Pointer.InflateMargins = True
      Pointer.SizeUnits = suAxis
      Pointer.Style = psCircle
      Pointer.VertSize = 1
      Pointer.Visible = True
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
      Data = {
        0019000000000000000000000000000000000891400000000000869040000000
        00005891400000000000D4924000000000004491400000000000DC8E40000000
        0000CC904000000000008E92400000000000B291400000000000309140000000
        0000188F400000000000A48F4000000000006890400000000000F89140000000
        0000B692400000000000DE924000000000002092400000000000E09040000000
        0000188F4000000000005E904000000000007691400000000000D69040000000
        00002A92400000000000849240}
      Detail = {0000000000}
    end
    object pole1: TLineSeries
      SeriesColor = clBlack
      Title = 'pole1'
      Brush.BackColor = clDefault
      LinePen.Visible = False
      OutLine.Style = psClear
      OutLine.Width = 0
      OutLine.Visible = True
      Pointer.Brush.Color = clHotLight
      Pointer.HorizSize = 3
      Pointer.InflateMargins = True
      Pointer.Pen.Width = 2
      Pointer.Style = psDiagCross
      Pointer.VertSize = 3
      Pointer.Visible = True
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
      Data = {
        00190000000000000000000000FFFFFFFFFF2F5E406266666666263840CCCCCC
        CCCCA85940666666666660644066666666666054409999999999214540999999
        99992155403333333333BC61403333333333BC61409899999999213540999999
        99995B614033333333334869409999999999AD6C406566666666605440FFFFFF
        FFFFFA604065666666669A6040FAFFFFFFFF2F4E40FAFFFFFFFFA34640060000
        0000304E40FAFFFFFFFF2F4E40FDFFFFFFFFA3564032333333330E6D40CCCCCC
        CCCCE2654099999999993E7340}
      Detail = {0000000000}
    end
    object pole2: TLineSeries
      SeriesColor = clBlack
      Title = 'pole2'
      Brush.BackColor = clDefault
      LinePen.Visible = False
      OutLine.Style = psClear
      OutLine.Width = 0
      OutLine.Visible = True
      Pointer.Brush.Color = clHotLight
      Pointer.HorizSize = 3
      Pointer.InflateMargins = True
      Pointer.Pen.Width = 2
      Pointer.Style = psDiagCross
      Pointer.VertSize = 3
      Pointer.Visible = True
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
      Data = {
        00190000000000000000000000FFFFFFFFFF2F5E406266666666263840CCCCCC
        CCCCA85940666666666660644066666666666054409999999999214540999999
        99992155403333333333BC61403333333333BC61409899999999213540999999
        99995B614033333333334869409999999999AD6C406566666666605440FFFFFF
        FFFFFA604065666666669A6040FAFFFFFFFF2F4E40FAFFFFFFFFA34640060000
        0000304E40FAFFFFFFFF2F4E40FDFFFFFFFFA3564032333333330E6D40CCCCCC
        CCCCE2654099999999993E7340}
    end
    object horizontal: TLineSeries
      SeriesColor = clBlack
      Brush.BackColor = clDefault
      LinePen.Width = 2
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
    object vertical: TLineSeries
      SeriesColor = clBlack
      Brush.BackColor = clDefault
      LinePen.Width = 2
      Pointer.InflateMargins = True
      Pointer.Style = psRectangle
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
    end
    object zero1: TLineSeries
      Selected.Hover.Visible = False
      SeriesColor = clWhite
      Title = 'zero1'
      Brush.BackColor = clDefault
      OutLine.Style = psDash
      OutLine.SmallDots = True
      Pointer.Brush.Style = bsClear
      Pointer.InflateMargins = True
      Pointer.Pen.Width = 2
      Pointer.Style = psCircle
      Pointer.Visible = True
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
      Transparency = 100
      Data = {
        0019000000000000000000E03F65666666666054409899999999E75840FFFFFF
        FFFFC06440CCCCCCCCCC8B6B400000000000DE72403333333333BC7140000000
        0000DE724000000000008778409A999999194D7240CECCCCCCCCA869409B9999
        9999906E4067666666666074403433333333486940CECCCCCCCC6E5D40010000
        0000DE524034333333332B5B40CECCCCCCCCE255409E99999999213540CDCCCC
        CCCC3960406766666666B24F400100000000304E40FCFFFFFFFF2F2E409A9999
        9999AD5C409A99999999AD6C40}
      Detail = {0000000000}
    end
    object zero2: TLineSeries
      Selected.Hover.Visible = False
      SeriesColor = clWhite
      Title = 'zero2'
      Brush.BackColor = clDefault
      OutLine.Style = psDash
      OutLine.SmallDots = True
      Pointer.Brush.Style = bsClear
      Pointer.HorizSize = 3
      Pointer.InflateMargins = True
      Pointer.Pen.Width = 2
      Pointer.Style = psCircle
      Pointer.VertSize = 3
      Pointer.Visible = True
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Y'
      YValues.Order = loNone
      Transparency = 100
      Data = {
        0019000000000000000000E03F65666666666054409899999999E75840FFFFFF
        FFFFC06440CCCCCCCCCC8B6B400000000000DE72403333333333BC7140000000
        0000DE724000000000008778409A999999194D7240CECCCCCCCCA869409B9999
        9999906E4067666666666074403433333333486940CECCCCCCCC6E5D40010000
        0000DE524034333333332B5B40CECCCCCCCCE255409E99999999213540CDCCCC
        CCCC3960406766666666B24F400100000000304E40FCFFFFFFFF2F2E409A9999
        9999AD5C409A99999999AD6C40}
    end
  end
  object ScrollBar1: TScrollBar
    Left = 8
    Top = 257
    Width = 179
    Height = 17
    Max = 10
    PageSize = 0
    TabOrder = 5
    OnChange = ScrollBar1Change
  end
  object ScrollBar2: TScrollBar
    Left = 8
    Top = 300
    Width = 179
    Height = 17
    Max = 180
    PageSize = 0
    TabOrder = 6
    OnChange = ScrollBar2Change
  end
  object Chart4: TChart
    Left = 8
    Top = 390
    Width = 394
    Height = 170
    Legend.Font.Color = 4210752
    Legend.Font.Height = -13
    Legend.Font.Name = 'Verdana'
    Legend.Frame.Visible = False
    Legend.Transparent = True
    Legend.Visible = False
    Title.Font.Color = clGray
    Title.Font.Height = -16
    Title.Text.Strings = (
      'Magnitude Response')
    BottomAxis.Grid.Visible = False
    BottomAxis.LabelsFormat.Font.Color = clGray
    BottomAxis.LabelsFormat.Font.Height = -13
    BottomAxis.LabelsFormat.Font.Name = 'Verdana'
    BottomAxis.MinorTicks.Visible = False
    BottomAxis.Title.Font.Color = 4210752
    BottomAxis.Title.Font.Height = -15
    DepthAxis.LabelsFormat.Font.Color = clGray
    DepthAxis.LabelsFormat.Font.Height = -13
    DepthAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthAxis.MinorTicks.Visible = False
    DepthAxis.Title.Font.Color = 4210752
    DepthAxis.Title.Font.Height = -15
    DepthTopAxis.LabelsFormat.Font.Color = clGray
    DepthTopAxis.LabelsFormat.Font.Height = -13
    DepthTopAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthTopAxis.MinorTicks.Visible = False
    DepthTopAxis.Title.Font.Color = 4210752
    DepthTopAxis.Title.Font.Height = -15
    LeftAxis.Axis.Visible = False
    LeftAxis.LabelsFormat.Font.Color = clGray
    LeftAxis.LabelsFormat.Font.Height = -13
    LeftAxis.LabelsFormat.Font.Name = 'Verdana'
    LeftAxis.MinorTicks.Visible = False
    LeftAxis.Title.Font.Color = 4210752
    LeftAxis.Title.Font.Height = -15
    RightAxis.LabelsFormat.Font.Color = clGray
    RightAxis.LabelsFormat.Font.Height = -13
    RightAxis.LabelsFormat.Font.Name = 'Verdana'
    RightAxis.MinorTicks.Visible = False
    RightAxis.Title.Font.Color = 4210752
    RightAxis.Title.Font.Height = -15
    TopAxis.LabelsFormat.Font.Color = clGray
    TopAxis.LabelsFormat.Font.Height = -13
    TopAxis.LabelsFormat.Font.Name = 'Verdana'
    TopAxis.MinorTicks.Visible = False
    TopAxis.Title.Font.Color = 4210752
    TopAxis.Title.Font.Height = -15
    View3D = False
    View3DWalls = False
    Color = clWhite
    TabOrder = 7
    DefaultCanvas = 'TGDIPlusCanvas'
    ColorPaletteIndex = 0
    object MagnitudeChart: TBarSeries
      BarBrush.BackColor = clDefault
      Marks.Brush.Color = 6868991
      Marks.Font.Name = 'Verdana'
      Marks.RoundSize = 0
      Marks.Shadow.Visible = False
      Marks.Visible = False
      Marks.Callout.Length = 8
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Bar'
      YValues.Order = loNone
    end
  end
  object Chart5: TChart
    Left = 408
    Top = 390
    Width = 387
    Height = 170
    Legend.Font.Color = 4210752
    Legend.Font.Height = -13
    Legend.Font.Name = 'Verdana'
    Legend.Frame.Visible = False
    Legend.Transparent = True
    Legend.Visible = False
    Title.Font.Color = clGray
    Title.Font.Height = -16
    Title.Text.Strings = (
      'Magnitude From Pantomkins')
    BottomAxis.Grid.Visible = False
    BottomAxis.LabelsFormat.Font.Color = clGray
    BottomAxis.LabelsFormat.Font.Height = -13
    BottomAxis.LabelsFormat.Font.Name = 'Verdana'
    BottomAxis.MinorTicks.Visible = False
    BottomAxis.Title.Font.Color = 4210752
    BottomAxis.Title.Font.Height = -15
    DepthAxis.LabelsFormat.Font.Color = clGray
    DepthAxis.LabelsFormat.Font.Height = -13
    DepthAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthAxis.MinorTicks.Visible = False
    DepthAxis.Title.Font.Color = 4210752
    DepthAxis.Title.Font.Height = -15
    DepthTopAxis.LabelsFormat.Font.Color = clGray
    DepthTopAxis.LabelsFormat.Font.Height = -13
    DepthTopAxis.LabelsFormat.Font.Name = 'Verdana'
    DepthTopAxis.MinorTicks.Visible = False
    DepthTopAxis.Title.Font.Color = 4210752
    DepthTopAxis.Title.Font.Height = -15
    LeftAxis.Axis.Visible = False
    LeftAxis.LabelsFormat.Font.Color = clGray
    LeftAxis.LabelsFormat.Font.Height = -13
    LeftAxis.LabelsFormat.Font.Name = 'Verdana'
    LeftAxis.MinorTicks.Visible = False
    LeftAxis.Title.Font.Color = 4210752
    LeftAxis.Title.Font.Height = -15
    RightAxis.LabelsFormat.Font.Color = clGray
    RightAxis.LabelsFormat.Font.Height = -13
    RightAxis.LabelsFormat.Font.Name = 'Verdana'
    RightAxis.MinorTicks.Visible = False
    RightAxis.Title.Font.Color = 4210752
    RightAxis.Title.Font.Height = -15
    TopAxis.LabelsFormat.Font.Color = clGray
    TopAxis.LabelsFormat.Font.Height = -13
    TopAxis.LabelsFormat.Font.Name = 'Verdana'
    TopAxis.MinorTicks.Visible = False
    TopAxis.Title.Font.Color = 4210752
    TopAxis.Title.Font.Height = -15
    View3D = False
    View3DWalls = False
    Color = clWhite
    TabOrder = 8
    DefaultCanvas = 'TGDIPlusCanvas'
    ColorPaletteIndex = 0
    object mag2chart: TBarSeries
      BarBrush.BackColor = clDefault
      Marks.Brush.Color = 6868991
      Marks.Font.Name = 'Verdana'
      Marks.RoundSize = 0
      Marks.Shadow.Visible = False
      Marks.Visible = False
      Marks.Callout.Length = 8
      XValues.Name = 'X'
      XValues.Order = loAscending
      YValues.Name = 'Bar'
      YValues.Order = loNone
    end
  end
end
