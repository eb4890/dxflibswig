import dxflib


class creationclass (dxflib.DL_CreationInterface):
 
  def __init__(self):
     dxflib.DL_CreationInterface.__init__(self) 
     print "init"

 #   pass

  def addLayer (self, layerdata):
     print "layer"

  def addBlock (self, blockdata):
     print "block" 

  def endBlock(self):
     print "end block"

  def addPoint(self, pointdata):
     print "addpoint"

  def addLine(self, linedata):
     #linedata.__disown__()
     print "before line data"
     print str(linedata.x1) + " " + str (linedata.x2)
     print "Hi"


  def addArc(self, arcdata):
    pass

  def addCircle(self, circledata):
    pass

  def addEllipse(self, ellipsedata):
    pass
  def addPolyline(self, polylinedata):
    pass
  def addVertex(self, vertexdata):
    pass
  def addSpline(self, splinedata):
    pass
	
  def addControlPoint(self, controldata):
    pass
	
  def addKnot(self, knotdata):
    pass

  def addInsert(self, insertdata): 
    pass
    
  def addTrace(self, tracedata):
    pass
    
  def add3dFace(self, facedata):
    pass
  def addSolid(self, soliddata):
    pass 


  def addMText(self, mtextdata):
    pass
  def addMTextChunk(self,  chartext):
    pass
  def addText(self, textdata):
    pass
  def addDimAlign( self, dimensiondata,
                              aligneddata):
    pass
  def addDimLinear( self, dimensiondata,
                               dimlineardata):
    pass
  def addDimRadial( self, dimensiondata,
                               DimRadialData):

    pass
  def addDimDiametric( self, DimensionData,
                               DimDiametricData):

    pass
  def addDimAngular( self, DimensionData,
                               DimAngularData):

    pass
  def addDimAngular3P( self, DimensionData,
                               DimAngular3PData):
	
    pass
  def addDimOrdinate( self, DimensionData,
                              DimOrdinateData):
    
    pass
     
	 
  def addLeader( self, LeaderData):
	
    pass
	 
	 
  def addLeaderVertex( self, LeaderVertexData):
	
    pass
	 
	 
  def addHatch(self,  HatchData):
	
    pass
	 
	 
  def addImage(self,  ImageData):

    pass
	
	 
  def linkImage(self,  ImageDefData):

    pass
	 
	 
  def addHatchLoop(self,  HatchLoopData):

    pass
	 
	 
  def addHatchEdge(self,  HatchEdgeData):
	
    pass
	 
	 
  def endEntity(self):
    
    pass
    
     
  def addComment(self, comment):

    pass
    
     
  def setVariableVector(self, key, v1, v2, v3, code): 
	
    pass
    
     
  def setVariableString(self, key, charvalue, code):
    print "hello"
    #pass
    
     
  def setVariableInt(self, key, intvalue, code):
	
    pass
    
     
  def setVariableDouble(self,  key, doublevalue, code): 
	
    pass
     
      
  def endSequence(self ):

    pass


creation = creationclass().__disown__()
d = dxflib.DL_Dxf()
d._in ("demo.dxf", creation)


