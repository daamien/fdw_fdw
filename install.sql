
CREATE EXTENSION multicorn;

CREATE SERVER fdw_fdw 
FOREIGN DATA WRAPPER multicorn
options (
  wrapper 'fdwfdw.FDWFDW'
);


CREATE FOREIGN TABLE wrappers (
	source TEXT,
	"type" TEXT,
    licence TEXT,
    code TEXT,
    install TEXT,
    doc TEXT,
    notes TEXT
) server fdw_fdw 
;


