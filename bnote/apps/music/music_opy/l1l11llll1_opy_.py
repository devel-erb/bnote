"""
Copyright (c)2021 eurobraille
This software is the proprietary of eurobraille and may not be copied,
distributed, published,or disclosed without express prior written permission.
"""

import mido
from .l1l111111l_opy_ import *
from .l1l11111l1_opy_ import *
from operator import itemgetter, attrgetter


class l1l1111l1l_opy_:
    def __init__(self, l1ll1l1ll_opy_):
        self._1ll1l11l_opy_ = l1ll1l1ll_opy_

    def create_file(self, l1l1l11111_opy_):
        """structure of a midi_track_event
        for program change : 0 = time counter, 1 = 1, 2 = 'program_change', 3 = value, 4 = 0 5 = 0
        for tempo 0 = time counter, 1 = 2, 2 = 'set_tempo', 3 = value, 4 = 0, 5 = 0
        for a note : 0 = time counter, 1 = 3, 2 = 'note_on' or 'note_off', 3 = midi_hight, 4 = velocity, 5 = duration, 6 = measure number, 7 = syllable
        for karaoke : 0 = time counter, 1 = 4, 2 = 'lyrics', 3 = text value, 4 = 0, 5 = 0
        events will be sorted according to time counter 0, message type 1, then message code 2
        """
        l1l11ll11l_opy_ = 1
        # print(mido.l1l1l1l111_opy_())
        tempo = int(480 / l1l11ll11l_opy_)
        l1l111lll1_opy_ = 115
        l1l1111ll1_opy_ = 0
        f = open("trace_midi2.txt", "w", encoding="utf-8")
        mid = mido.MidiFile()
        l1l111l11l_opy_ = 0
        l1l11lll11_opy_ = list()
        for element in self._1ll1l11l_opy_.l1l111l111_opy_:
            if element.t == "part-list":
                for item in element.l1l1l1lll1_opy_:
                    if item.l1l1l11l11_opy_ != "no":
                        l1l1l11l11_opy_ = item.l1l1l11l11_opy_
                    else:
                        l1l1l11l11_opy_ = "1"
                    if item.l1l11l11ll_opy_ != "no":
                        l1l11l11ll_opy_ = item.l1l11l11ll_opy_
                    else:
                        l1l11l11ll_opy_ = "1"
                    if item.l1l1111111_opy_ != "no":
                        l1l1111111_opy_ = item.l1l1111111_opy_
                    else:
                        l1l1111111_opy_ = "80"
                    l1l11lll11_opy_.append(
                        [
                            int(l1l1l11l11_opy_) - 1,
                            int(l1l11l11ll_opy_) - 1,
                            int(l1l1111111_opy_.split(".")[0]),
                        ]
                    )
            if element.t == "part":
                l1l11l11l1_opy_ = 0
                l1l111l11l_opy_ += 1
                l1l1l1l11l_opy_ = list()
                l1l111llll_opy_ = mido.MidiTrack()
                mid.tracks.append(l1l111llll_opy_)
                l1l11l1111_opy_ = 0
                l1l1l1l11l_opy_.append(
                    [
                        l1l11l1111_opy_,
                        1,
                        "program_change",
                        l1l11lll11_opy_[l1l111l11l_opy_ - 1][0],
                        0,
                        0,
                    ]
                )
                l1l1l1l11l_opy_.append(
                    [
                        l1l11l1111_opy_,
                        1,
                        "control_change",
                        l1l11lll11_opy_[l1l111l11l_opy_ - 1][2],
                        7,
                        0,
                    ]
                )
                l1l1l111l1_opy_ = False
                for l1l11l111l_opy_ in element.l1l1l1ll1l_opy_:
                    for event in l1l11l111l_opy_.l1l11ll1l1_opy_:
                        if event.t == "note":
                            if not event.rest:
                                midi_hight = (
                                    12
                                    + event.l1l11ll111_opy_ * 12
                                    + l1l1l11l1l_opy_[event.step]
                                    + l1l11l11l1_opy_
                                )
                                if event.l1l111ll11_opy_:
                                    midi_hight += l1l111ll1l_opy_[event.l1l111ll11_opy_]
                            if (
                                not event.rest
                                and l1l1l111l1_opy_
                                and event.l1l11ll1ll_opy_ == "start"
                            ):
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_ - event.l1l1111l11_opy_,
                                        3,
                                        "note_on",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        event.l1l1111l11_opy_,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        event.text,
                                    ]
                                )
                            elif not event.rest and event.l1l111l1ll_opy_:
                                pass
                                # l1l1l1l11l_opy_.append([l1l11l1111_opy_, 3, 'note_on', midi_hight, l1l111lll1_opy_, 1, l1l11l111l_opy_.l1l1l1ll11_opy_, event.text])
                                # l1l1l1l11l_opy_.append([l1l11l1111_opy_, 3, 'note_off', midi_hight, l1l111lll1_opy_, 0, l1l11l111l_opy_.l1l1l1ll11_opy_, ""])
                            elif (
                                not event.rest
                                and l1l1l111l1_opy_
                                and event.l1l11ll1ll_opy_ == "stop"
                            ):
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_,
                                        3,
                                        "note_off",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        0,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        "",
                                    ]
                                )
                            elif (
                                not event.rest
                                and l1l1l111l1_opy_
                                and event.l1l11ll1ll_opy_ == "no"
                            ):
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_ - event.l1l1111l11_opy_,
                                        3,
                                        "note_on",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        event.l1l1111l11_opy_,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        event.text,
                                    ]
                                )
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_,
                                        3,
                                        "note_off",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        0,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        "",
                                    ]
                                )
                            elif (
                                not event.rest
                                and not event.l1l1l1l1ll_opy_
                                and not event.l1l1l11ll1_opy_
                            ):
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_,
                                        3,
                                        "note_on",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        0,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        event.text,
                                    ]
                                )
                                if l1l1111lll_opy_.l1l11l1ll1_opy_:
                                    l1l1l1l11l_opy_.append(
                                        [l1l11l1111_opy_, 4, "lyrics", event.text, 0, 0]
                                    )
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_ + event.l1l1111l11_opy_,
                                        3,
                                        "note_off",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        event.l1l1111l11_opy_,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        "",
                                    ]
                                )
                                l1l11l1111_opy_ += event.l1l1111l11_opy_
                            elif (
                                not event.rest
                                and not event.l1l1l1l1ll_opy_
                                and event.l1l1l11ll1_opy_
                            ):
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_ - event.l1l1111l11_opy_,
                                        3,
                                        "note_on",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        0,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        event.text,
                                    ]
                                )
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_,
                                        3,
                                        "note_off",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        0,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        "",
                                    ]
                                )
                            elif (
                                not event.rest
                                and event.l1l11ll1ll_opy_ == "start"
                                and not event.l1l1l11ll1_opy_
                            ):
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_,
                                        3,
                                        "note_on",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        0,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        event.text,
                                    ]
                                )
                                if l1l1111lll_opy_.l1l11l1ll1_opy_:
                                    l1l1l1l11l_opy_.append(
                                        [l1l11l1111_opy_, 4, "lyrics", event.text, 0, 0]
                                    )
                                l1l11l1111_opy_ += event.l1l1111l11_opy_
                                l1l1111ll1_opy_ += event.l1l1111l11_opy_
                            elif (
                                not event.rest
                                and event.l1l11ll1ll_opy_ == "start"
                                and event.l1l1l11ll1_opy_
                            ):
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_ - event.l1l1111l11_opy_,
                                        3,
                                        "note_on",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        0,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        event.text,
                                    ]
                                )
                            elif (
                                not event.rest
                                and event.l1l11ll1ll_opy_ == "stop-start"
                                and not event.l1l1l11ll1_opy_
                            ):
                                l1l11l1111_opy_ += event.l1l1111l11_opy_
                                l1l1111ll1_opy_ += event.l1l1111l11_opy_
                            elif (
                                not event.rest
                                and event.l1l11ll1ll_opy_ == "stop-start"
                                and event.l1l1l11ll1_opy_
                            ):
                                l1l1111ll1_opy_ += event.l1l1111l11_opy_
                            elif (
                                not event.rest
                                and event.l1l11ll1ll_opy_ == "stop"
                                and not event.l1l1l11ll1_opy_
                            ):
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_ + event.l1l1111l11_opy_,
                                        3,
                                        "note_off",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        l1l1111ll1_opy_ + event.l1l1111l11_opy_,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        "",
                                    ]
                                )
                                l1l11l1111_opy_ += event.l1l1111l11_opy_
                                l1l1111ll1_opy_ = 0
                            elif (
                                not event.rest
                                and event.l1l11ll1ll_opy_ == "stop"
                                and event.l1l1l11ll1_opy_
                            ):
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_,
                                        3,
                                        "note_off",
                                        midi_hight,
                                        l1l111lll1_opy_,
                                        0,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        "",
                                    ]
                                )
                            if event.rest:
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_,
                                        3,
                                        "note_on",
                                        1,
                                        0,
                                        0,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        event.text,
                                    ]
                                )
                                l1l1l1l11l_opy_.append(
                                    [
                                        l1l11l1111_opy_ + event.l1l1111l11_opy_,
                                        3,
                                        "note_off",
                                        1,
                                        0,
                                        event.l1l1111l11_opy_,
                                        l1l11l111l_opy_.l1l1l1ll11_opy_,
                                        "",
                                    ]
                                )
                                l1l11l1111_opy_ += event.l1l1111l11_opy_
                            if event.l1l1l1l1ll_opy_ and event.l1l11l1l11_opy_ == 1:
                                l1l1l111l1_opy_ = True
                            elif event.l1l11l1l11_opy_ == 3 and l1l1l111l1_opy_:
                                l1l1l111l1_opy_ = False
                        elif event.t == "backup":
                            l1l11l1111_opy_ -= event.l1l1111l11_opy_
                        elif event.t == "attributes":
                            for l1l111l1l1_opy_ in event.l1l1l111ll_opy_:
                                if l1l111l1l1_opy_.t == "divisions":
                                    l1l11ll11l_opy_ = l1l111l1l1_opy_.l1l11ll11l_opy_
                                    tempo = int(480 / l1l11ll11l_opy_)
                                elif l1l111l1l1_opy_.t == "transpose":
                                    l1l11l11l1_opy_ = (
                                        l1l111l1l1_opy_.l1l1l11lll_opy_
                                        + 12 * l1l111l1l1_opy_.l11lllll11_opy_
                                    )
                        elif event.t == "direction":
                            for l1l111l1l1_opy_ in event.l1l11lllll_opy_:
                                if l1l111l1l1_opy_.t == "sound":
                                    if l1l111l1l1_opy_.l1l1l1111l_opy_ != "no":
                                        l1l1l1l11l_opy_.append(
                                            [
                                                l1l11l1111_opy_,
                                                2,
                                                "set_tempo",
                                                int(
                                                    1000000
                                                    * 60
                                                    / int(
                                                        l1l111l1l1_opy_.l1l1l1111l_opy_
                                                    )
                                                ),
                                                0,
                                                0,
                                            ]
                                        )
                                elif l1l111l1l1_opy_.t == "dynamics":
                                    l1l111lll1_opy_ = l1l11111ll_opy_[
                                        l1l111l1l1_opy_.l1l11lll1l_opy_
                                    ]
                                elif l1l111l1l1_opy_.t == "metronome":
                                    l1l1l1l11l_opy_.append(
                                        [
                                            l1l11l1111_opy_,
                                            2,
                                            "set_tempo",
                                            int(
                                                1000000
                                                * 60
                                                / int(l1l111l1l1_opy_.l1l11l1lll_opy_)
                                            ),
                                            0,
                                            0,
                                        ]
                                    )
                        elif event.t == "karaoke" and l1l1111lll_opy_.l11lllllll_opy_:
                            l1l1l1l11l_opy_.append(
                                [
                                    l1l11l1111_opy_,
                                    4,
                                    "lyrics",
                                    event.l1l1l1l1l1_opy_,
                                    0,
                                    0,
                                ]
                            )
                f.write(str(l1l1l1l11l_opy_))
                l11llllll1_opy_ = sorted(l1l1l1l11l_opy_, key=itemgetter(0, 1, 2))
                f.write("\ntriée\n" + str(l11llllll1_opy_))
                l1l11l1l1l_opy_ = 0
                for l11lllll1l_opy_ in l11llllll1_opy_:
                    l1l11l1l1l_opy_ += l11lllll1l_opy_[5]
                    if l1l11l1l1l_opy_ > l11lllll1l_opy_[0]:
                        l11lllll1l_opy_[5] = l11lllll1l_opy_[0] - (
                            l1l11l1l1l_opy_ - l11lllll1l_opy_[5]
                        )
                        l1l11l1l1l_opy_ = l11lllll1l_opy_[0]
                f.write("\narrangée\n" + str(l11llllll1_opy_))
                f.write("\ntrack\n")
                for message in l11llllll1_opy_:
                    f.write(
                        str(message[0])
                        + " "
                        + str(message[1])
                        + " "
                        + str(message[2])
                        + " "
                        + str(message[3])
                        + " "
                        + str(message[4])
                        + " "
                        + str(message[5])
                        + "\n"
                    )
                    if message[1] == 3:
                        l1l111llll_opy_.append(
                            mido.Message(
                                message[2],
                                note=message[3],
                                velocity=message[4],
                                time=message[5] * tempo,
                                channel=l1l11lll11_opy_[l1l111l11l_opy_ - 1][1],
                            )
                        )
                    elif message[1] == 2:
                        l1l111llll_opy_.append(
                            mido.MetaMessage(
                                message[2], tempo=message[3], time=message[4]
                            )
                        )
                    elif message[1] == 4:
                        l1l111llll_opy_.append(
                            mido.MetaMessage(
                                message[2], text=message[3], time=message[4]
                            )
                        )
                    elif message[1] == 1 and message[2] == "program_change":
                        l1l111llll_opy_.append(
                            mido.Message(
                                message[2],
                                program=message[3],
                                channel=l1l11lll11_opy_[l1l111l11l_opy_ - 1][1],
                            )
                        )
                    elif message[1] == 1 and message[2] == "control_change":
                        l1l111llll_opy_.append(
                            mido.Message(
                                message[2],
                                control=message[4],
                                value=message[3],
                                channel=l1l11lll11_opy_[l1l111l11l_opy_ - 1][1],
                            )
                        )
        mid.save(l1l1l11111_opy_)