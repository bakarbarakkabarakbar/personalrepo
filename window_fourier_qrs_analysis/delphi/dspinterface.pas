unit dspinterface;

interface


type
   vektor=array[0..10000] of real;
   matrik=array[0..10000,0..5] of real;


function invdft(n:integer;re,im:array of real):vektor;stdcall;
function fft(t,n:integer;xr,xi:array of real):matrik;stdcall;
function dft(n:integer;s:array of real):matrik;stdcall;


implementation


function invdft;external 'mydsp.dll' Name 'invdft';stdcall;
function fft;external 'mydsp.dll' Name 'fft';stdcall;
function dft;external 'mydsp.dll' Name 'dft'; stdcall;




end.
 