

%module(directors="1") dxflib 

%{


#include "dl_attributes.h"
#include "dl_codes.h"
#include "dl_entities.h"
#include "dl_writer.h"
#include "dl_writer_ascii.h"
#include "dl_creationinterface.h"
#include "dl_creationadapter.h"
#include "dl_dxf.h"
%}
%include stl.i
%feature ("director");
%include "dl_dxf.h"
%include "dl_attributes.h"
%include "dl_codes.h"
%include "dl_entities.h"
%include "dl_writer.h"
%include "dl_writer_ascii.h"
%include "dl_creationinterface.h"
%include "dl_creationadapter.h"
%include "std_string.i"
// EOF
