#ifndef ST_SAVE_H
#define ST_SAVE_H

#include "state.h"

extern struct state st_save;
extern struct state st_clobber;

int goto_save(struct state *, struct state *);

#endif
