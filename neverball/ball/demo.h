#ifndef DEMO_H
#define DEMO_H

#include <time.h>
#include <stdio.h>

#include "level.h"
#include "fs.h"

/*---------------------------------------------------------------------------*/

struct demo
{
    char   path[MAXSTR];                /* Demo path                         */
    char   name[PATHMAX];               /* Demo basename                     */

    char   player[MAXSTR];
    time_t date;

    int    timer;
    int    coins;
    int    status;
    int    mode;

    char   shot[PATHMAX];               /* Image filename                    */
    char   file[PATHMAX];               /* Level filename                    */

    int    time;                        /* Time limit                        */
    int    goal;                        /* Coin limit                        */
    int    score;                       /* Total coins                       */
    int    balls;                       /* Number of balls                   */
    int    times;                       /* Total time                        */

};

/*---------------------------------------------------------------------------*/

int  demo_load(struct demo *, const char *);
void demo_free(struct demo *);

int demo_exists(const char *);

const char *demo_format_name(const char *fmt,
                             const char *set,
                             const char *level);

/*---------------------------------------------------------------------------*/

int  demo_play_init(const char *, const struct level *, int, int, int, int);
void demo_play_step(void);
void demo_play_stat(int, int, int);
void demo_play_stop(int);

int  demo_saved (void);
void demo_rename(const char *);

void demo_rename_player(const char *name, const char *player);

/*---------------------------------------------------------------------------*/

int  demo_replay_init(const char *, int *, int *, int *, int *, int *);
int  demo_replay_step(float);
void demo_replay_stop(int);
float demo_replay_blend(void);

const char *curr_demo(void);

void demo_replay_speed(int);

/*---------------------------------------------------------------------------*/

extern fs_file demo_fp;

/*---------------------------------------------------------------------------*/

#endif
