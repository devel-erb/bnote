"""
Copyright (c)2021 eurobraille
This software is the proprietary of eurobraille and may not be copied,
distributed, published,or disclosed without express prior written permission.
"""

import xml.etree.ElementTree as l1ll11ll1lll_opy_
from xml.dom import minidom
from .l11l1ll1lll_opy_ import *
import time


# import l111l1llll1_opy_.__init__ as version
class l1l1l1l1l_opy_:
    def __init__(self, l1l1llll1ll_opy_, l1ll1l111ll1_opy_, l1ll1l1ll_opy_):
        self._1l1l1lll_opy_ = l1l1llll1ll_opy_
        self._1l11l11l_opy_ = l1ll1l111ll1_opy_
        self._1ll1l11l_opy_ = l1ll1l1ll_opy_

    def create_file(self, l1l11l1ll_opy_):
        t1 = time.time()
        l11l1l111l_opy_ = False
        if l11l1l111l_opy_:
            self._1l11l11l_opy_("\nmodel to xml\n")
        root = l1ll11ll1lll_opy_.Element("score-partwise")
        root.attrib = {"version": "4.0"}
        l1ll1l11ll11_opy_ = l1ll11ll1lll_opy_.SubElement(root, "identification")
        l1l1llllll11_opy_ = l1ll11ll1lll_opy_.SubElement(l1ll1l11ll11_opy_, "encoding")
        l1ll1ll1l1ll_opy_ = l1ll11ll1lll_opy_.SubElement(
            l1l1llllll11_opy_, "software"
        ).text = ("eurobraille b.note " + version.__version__)
        l1ll1ll11111_opy_ = l1ll11ll1lll_opy_.SubElement(root, "defaults")
        l1ll1111ll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
            l1ll1ll11111_opy_, "lyric-font"
        )
        l1ll1111ll1l_opy_.attrib = {"font-family": "Times New Roman"}
        l1ll1111ll11_opy_ = False
        l1ll1l1l1ll1_opy_ = False
        for element in self._1ll1l11l_opy_.l1l111l111_opy_:
            if element.t == "part":
                l1ll1l1ll11l_opy_ = l1ll11ll1lll_opy_.SubElement(root, "part")
                l1ll1l1ll11l_opy_.attrib = {"id": element.l111ll1ll1l_opy_}
                for l1l11l111l_opy_ in element.l1l1l1ll1l_opy_:
                    l1ll111111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                        l1ll1l1ll11l_opy_, "measure"
                    )
                    l1ll111111l1_opy_.attrib = {
                        "number": str(l1l11l111l_opy_.l1l1l1ll11_opy_)
                    }
                    l1ll11ll111l_opy_ = False
                    l1ll1l11llll_opy_ = False
                    l1l1llllll1l_opy_ = False
                    l1ll111111ll_opy_ = False
                    l1ll1l11l111_opy_ = False
                    l1lll1111ll1_opy_ = False
                    l1ll1l1l1lll_opy_ = False
                    for event in l1l11l111l_opy_.l1l11ll1l1_opy_:
                        l1l1llll1l1l_opy_ = False
                        if event.t == "attributes":
                            for l1l111l1l1_opy_ in event.l1l1l111ll_opy_:
                                if l1l111l1l1_opy_.t == "divisions":
                                    l1ll11ll111l_opy_ = True
                                    l1ll111l1ll1_opy_ = str(
                                        l1l111l1l1_opy_.l1l11ll11l_opy_
                                    )
                                elif l1l111l1l1_opy_.t == "key":
                                    l1ll1l11llll_opy_ = True
                                    l1ll1l111lll_opy_ = str(
                                        l1l111l1l1_opy_.l11l11l111l_opy_
                                    )
                                    l1ll11l111ll_opy_ = l1l111l1l1_opy_.mode
                                elif l1l111l1l1_opy_.t == "time":
                                    l1l1llllll1l_opy_ = True
                                    l1ll11lll11l_opy_ = l1l111l1l1_opy_.l1111ll1111_opy_
                                    l1ll1111l11l_opy_ = l1l111l1l1_opy_.l1111ll11l1_opy_
                                    l1ll11ll1ll1_opy_ = l1l111l1l1_opy_.l1111lll1l1_opy_
                                elif l1l111l1l1_opy_.t == "staves":
                                    l1ll111111ll_opy_ = True
                                    l1ll1l1l1l11_opy_ = l1l111l1l1_opy_.l1l1l1l1ll1_opy_
                                elif l1l111l1l1_opy_.t == "clef":
                                    l1ll1l11l111_opy_ = True
                                    l1ll1111llll_opy_ = l1l111l1l1_opy_.sign
                                    l1ll1l1l11l1_opy_ = l1l111l1l1_opy_.line
                                    l1ll111l1l11_opy_ = l1l111l1l1_opy_.l111l1ll1l1_opy_
                                    l1ll1ll1l11l_opy_ = l1l111l1l1_opy_.l111lllll11_opy_
                                elif l1l111l1l1_opy_.t == "transpose":
                                    l1lll1111ll1_opy_ = True
                                    l1ll1l1l1l1l_opy_ = str(
                                        l1l111l1l1_opy_.l111lllll1l_opy_
                                    )
                                    l1ll11111l1l_opy_ = str(
                                        l1l111l1l1_opy_.l1l1l11lll_opy_
                                    )
                                    l1ll1ll1lll1_opy_ = str(
                                        l1l111l1l1_opy_.l11lllll11_opy_
                                    )
                                    l1ll11l11l1l_opy_ = l1l111l1l1_opy_.l111l11l1l1_opy_
                                    l1ll1ll111ll_opy_ = l1l111l1l1_opy_.l111l1111l1_opy_
                        else:
                            if (
                                l1ll11ll111l_opy_
                                or l1ll1l11llll_opy_
                                or l1l1llllll1l_opy_
                                or l1ll111111ll_opy_
                                or l1ll1l11l111_opy_
                                or l1lll1111ll1_opy_
                            ):
                                l1ll1ll1l1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll111111l1_opy_, "attributes"
                                )
                                if l1ll11ll111l_opy_:
                                    l1ll1l111l1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1l1l1_opy_, "divisions"
                                    ).text = l1ll111l1ll1_opy_
                                    l1ll11ll111l_opy_ = False
                                if l1ll1l11llll_opy_:
                                    l1ll11lll1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1l1l1_opy_, "key"
                                    )
                                    l1ll1ll11l11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll11lll1l1_opy_, "fifths"
                                    ).text = l1ll1l111lll_opy_
                                    if l1ll11l111ll_opy_ != "no":
                                        l1ll11ll1l11_opy_ = (
                                            l1ll11ll1lll_opy_.SubElement(
                                                l1ll11lll1l1_opy_, "mode"
                                            ).text
                                        ) = (l1ll11l111ll_opy_)
                                    l1ll1l11llll_opy_ = False
                                if l1l1llllll1l_opy_:
                                    l1ll111lll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1l1l1_opy_, "time"
                                    )
                                    l1ll111ll1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll111lll1l_opy_, "beats"
                                    ).text = l1ll11lll11l_opy_
                                    l1ll1111l111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll111lll1l_opy_, "beat-type"
                                    ).text = l1ll1111l11l_opy_
                                    if l1ll11ll1ll1_opy_ != "no":
                                        l1ll111lll1l_opy_.attrib = {
                                            "symbol": l1ll11ll1ll1_opy_
                                        }
                                    l1l1llllll1l_opy_ = False
                                if l1ll111111ll_opy_:
                                    l1ll11lll111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1l1l1_opy_, "staves"
                                    ).text = l1ll1l1l1l11_opy_
                                    l1ll111111ll_opy_ = False
                                if l1ll1l11l111_opy_:
                                    l1ll1l11l1ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1l1l1_opy_, "clef"
                                    )
                                    l1ll11l1111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1l11l1ll_opy_, "sign"
                                    ).text = l1ll1111llll_opy_
                                    l1ll1111l1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1l11l1ll_opy_, "line"
                                    ).text = l1ll1l1l11l1_opy_
                                    if l1ll111l1l11_opy_ != "no":
                                        l1ll1l11l11l_opy_ = (
                                            l1ll11ll1lll_opy_.SubElement(
                                                l1ll1l11l1ll_opy_, "clef-octave-change"
                                            ).text
                                        ) = (l1ll111l1l11_opy_)
                                    if l1ll1ll1l11l_opy_ != "no":
                                        l1ll111llll1_opy_ = (
                                            l1ll11ll1lll_opy_.SubElement(
                                                l1ll1l11l1ll_opy_, "braille-clef"
                                            ).text
                                        ) = (l1ll1ll1l11l_opy_)
                                    l1ll1l11l111_opy_ = False
                                if l1lll1111ll1_opy_:
                                    l1ll11111ll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1l1l1_opy_, "transpose"
                                    )
                                    l1ll111l111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll11111ll1_opy_, "diatonic"
                                    ).text = l1ll1l1l1l1l_opy_
                                    l1ll111l1111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll11111ll1_opy_, "chromatic"
                                    ).text = l1ll11111l1l_opy_
                                    l1ll11l1l11l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll11111ll1_opy_, "octave-change"
                                    ).text = l1ll1ll1lll1_opy_
                                    if l1ll11l11l1l_opy_:
                                        l1l1llll1ll1_opy_ = (
                                            l1ll11ll1lll_opy_.SubElement(
                                                l1ll11111ll1_opy_, "double"
                                            )
                                        )
                                        if l1ll1ll111ll_opy_ != "":
                                            l1l1llll1ll1_opy_.attrib = {
                                                "above": l1ll1ll111ll_opy_
                                            }
                                    l1lll1111ll1_opy_ = False
                        if event.t == "note":
                            l1ll1l1l11ll_opy_ = False
                            l1ll1ll1111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                l1ll111111l1_opy_, "note"
                            )
                            if event.l1l111l1ll_opy_:
                                l1ll1l11l1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "grace"
                                )
                                if event.l11lll1l1ll_opy_ != "missing":
                                    l1ll1l11l1l1_opy_.attrib = {
                                        "slash": event.l11lll1l1ll_opy_
                                    }
                            if event.l1l1l11ll1_opy_:
                                l1ll1l11111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "chord"
                                )
                            if event.step != "no":
                                l1l1lll1lll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "pitch"
                                )
                                l1ll1l1l111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1l1lll1lll1_opy_, "step"
                                ).text = l11l1ll11l1_opy_[event.step]
                            if event.l1l111ll11_opy_ != "no":
                                l1ll11l1l1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1l1lll1lll1_opy_, "alter"
                                ).text = l11l1ll11ll_opy_[event.l1l111ll11_opy_]
                            if event.l1l11ll111_opy_ != 100:
                                l1ll1ll1ll11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1l1lll1lll1_opy_, "octave"
                                ).text = str(event.l1l11ll111_opy_)
                            if event.rest:
                                l1ll111l1l1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "rest"
                                )
                            if event.l1l1111l11_opy_ != 0:
                                l1ll1l1lllll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "duration"
                                ).text = str(event.l1l1111l11_opy_)
                            if event.l1l1l1l1ll_opy_:
                                l1l1llll111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "tie"
                                )
                                if event.l1l11ll1ll_opy_ in ["start", "stop"]:
                                    l1l1llll111l_opy_.attrib = {
                                        "type": event.l1l11ll1ll_opy_
                                    }
                                elif event.l1l11ll1ll_opy_ == "stop-start":
                                    l1l1llll111l_opy_.attrib = {"type": "stop"}
                                    l1l1llll111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "tie"
                                    )
                                    l1l1llll111l_opy_.attrib = {"type": "start"}
                            if event.l1111ll11ll_opy_ != 0:
                                l1l1lll1ll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "voice"
                                ).text = str(event.l1111ll11ll_opy_)
                            if event.type != "no":
                                l1ll1l1ll1ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "type"
                                ).text = l11l1lll11l_opy_[event.type]
                            if event.dot:
                                l1ll111ll111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "dot"
                                )
                            if event.l111llllll_opy_ != "no":
                                l1ll1111l1ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "accidental"
                                ).text = event.l111llllll_opy_
                            if (
                                event.l1111lll1ll_opy_ != 0
                                and event.l11l11111ll_opy_ != 0
                            ):
                                l1ll11l11lll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "time-modification"
                                )
                                l1ll11111l11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll11l11lll_opy_, "actual-notes"
                                ).text = str(event.l1111lll1ll_opy_)
                                l1ll11llll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll11l11lll_opy_, "normal-notes"
                                ).text = str(event.l11l11111ll_opy_)
                            if event.l11l1111ll1_opy_ != "no":
                                l1ll1111lll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "staff"
                                ).text = str(event.l11l1111ll1_opy_)
                            if event.l1l1l1l1ll_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll11l11ll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "tied"
                                )
                                if event.l1l11ll1ll_opy_ in ["start", "stop"]:
                                    l1ll11l11ll1_opy_.attrib = {
                                        "type": event.l1l11ll1ll_opy_
                                    }
                                elif event.l1l11ll1ll_opy_ == "stop-start":
                                    l1ll11l11ll1_opy_.attrib = {"type": "stop"}
                                    l1ll11l11ll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll111l1_opy_, "tied"
                                    )
                                    l1ll11l11ll1_opy_.attrib = {"type": "start"}
                            if event.l1l1l1lll1l_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll1l1111ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "slur"
                                )
                                if event.l11l11l1ll_opy_ != "no":
                                    l1ll1l1111ll_opy_.attrib = {
                                        "type": event.l11l11l1ll_opy_
                                    }
                                if event.l11l11lll1l_opy_ != "no":
                                    l1ll1l1111ll_opy_.attrib.update(
                                        {"number": event.l11l11lll1l_opy_}
                                    )
                                if event.l1l1l1ll1ll_opy_ != "no":
                                    l1ll1l1111ll_opy_.attrib.update(
                                        {"placement": event.l1l1l1ll1ll_opy_}
                                    )
                            if event.l111lllllll_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll1l1111ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "slur"
                                )
                                if event.l111ll11111_opy_ != "no":
                                    l1ll1l1111ll_opy_.attrib = {
                                        "type": event.l111ll11111_opy_
                                    }
                                if event.l1111l1llll_opy_ != "no":
                                    l1ll1l1111ll_opy_.attrib.update(
                                        {"number": event.l1111l1llll_opy_}
                                    )
                                if event.l111l1lllll_opy_ != "no":
                                    l1ll1l1111ll_opy_.attrib.update(
                                        {"placement": event.l111l1lllll_opy_}
                                    )
                            if event.l1ll1l11111_opy_ != "no":
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll11l1l111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "technical"
                                )
                                l1ll11lllll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll11l1l111_opy_, "fingering"
                                ).text = event.l1ll1l11111_opy_
                            if event.l111l1l1ll1_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll111lll11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "articulations"
                                )
                                l1ll11l1llll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll111lll11_opy_, "staccato"
                                )
                            if event.l11l11llll1_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll111lll11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "articulations"
                                )
                                l1ll1l11ll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll111lll11_opy_, "staccatissimo"
                                )
                            if event.l111l111ll1_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll111lll11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "articulations"
                                )
                                l1ll11llll11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll111lll11_opy_, "accent"
                                )
                            if event.l11l111ll1l_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll111lll11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "articulations"
                                )
                                l1ll11111lll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll111lll11_opy_, "breath-mark"
                                )
                            if event.l11l111l111_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll11l111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "fermata"
                                )
                            if event.l111l1111ll_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll111lllll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "ornaments"
                                )
                                l1ll111l11ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll111lllll_opy_, "trill-mark"
                                )
                            if event.l1111l1ll11_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll111lllll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "ornaments"
                                )
                                l1ll1ll1l111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll111lllll_opy_, "inverted-mordent"
                                )
                                l1ll1ll1l111_opy_.attrib = {
                                    "placement": event.l111ll1l1ll_opy_
                                }
                                l1ll1ll1l111_opy_.attrib = {
                                    "long": event.l1111ll111l_opy_
                                }
                            if event.l11l11l1l1l_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll111lllll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "ornaments"
                                )
                                l1ll111ll11l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll111lllll_opy_, "mordent"
                                )
                                l1ll111ll11l_opy_.attrib = {
                                    "placement": event.l1111lll111_opy_
                                }
                                l1ll111ll11l_opy_.attrib = {
                                    "long": event.l11l11lllll_opy_
                                }
                            if event.l11l11ll11l_opy_ or (
                                not l1l11l1ll_opy_ and event.l11l1l1111l_opy_
                            ):
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll11ll1l1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "arpeggiate"
                                )
                                if event.l1111lll11l_opy_ == "down" or (
                                    not l1l11l1ll_opy_
                                    and event.l111ll1ll11_opy_ == "down"
                                ):
                                    l1ll11ll1l1l_opy_.attrib = {"direction": "down"}
                            if l1l11l1ll_opy_ and event.l11l1l1111l_opy_:
                                if not l1ll1l1l11ll_opy_:
                                    l1ll1ll111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1ll1111l_opy_, "notations"
                                    )
                                    l1ll1l1l11ll_opy_ = True
                                l1ll1l111111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll111l1_opy_, "two-hands-arpeggiate"
                                )
                                if event.l111ll1ll11_opy_ == "down":
                                    l1ll1l111111_opy_.attrib = {"direction": "down"}
                            if event.text != "":
                                l1l1lll1l1ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1ll1111l_opy_, "lyric"
                                )
                                l1ll1l1ll111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1l1lll1l1ll_opy_, "syllabic"
                                ).text = event.l111llll1l1_opy_
                                l1ll1ll11lll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1l1lll1l1ll_opy_, "text"
                                ).text = event.text
                        elif event.t == "direction":
                            l1ll1l1llll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                l1ll111111l1_opy_, "direction"
                            )
                            if event.l111ll1111l_opy_ != "no":
                                l1ll1l1llll1_opy_.attrib = {
                                    "placement": event.l111ll1111l_opy_
                                }
                            for l1l111l1l1_opy_ in event.l1l11lllll_opy_:
                                if l1l111l1l1_opy_.t == "dynamics":
                                    l1ll1111111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1l1llll1_opy_, "direction-type"
                                    )
                                    l1ll111l11l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1111111l_opy_, "dynamics"
                                    )
                                    l1ll1l1lll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll111l11l1_opy_,
                                        l1l111l1l1_opy_.l1l11lll1l_opy_,
                                    )
                                if l1l111l1l1_opy_.t == "pedal":
                                    l1ll1111111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1l1llll1_opy_, "direction-type"
                                    )
                                    l1ll111l1lll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1111111l_opy_, "pedal"
                                    )
                                    l1ll111l1lll_opy_.attrib = {
                                        "type": l1l111l1l1_opy_.l11l11lll11_opy_
                                    }
                                if l1l111l1l1_opy_.t == "wedge":
                                    l1ll1111111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1l1llll1_opy_, "direction-type"
                                    )
                                    l1ll11111111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1111111l_opy_, "wedge"
                                    )
                                    l1ll11111111_opy_.attrib = {
                                        "type": l1l111l1l1_opy_.l1111l1l1ll_opy_
                                    }
                                if l1l111l1l1_opy_.t == "metronome":
                                    l1ll1111111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1l1llll1_opy_, "direction-type"
                                    )
                                    l1l1lllll1ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1111111l_opy_, "metronome"
                                    )
                                    if l1l111l1l1_opy_.l111ll1l111_opy_ != "no":
                                        l1ll11ll11l1_opy_ = (
                                            l1ll11ll1lll_opy_.SubElement(
                                                l1l1lllll1ll_opy_, "beat-unit"
                                            ).text
                                        ) = (l1l111l1l1_opy_.l111ll1l111_opy_)
                                    if l1l111l1l1_opy_.l111lll11l1_opy_:
                                        l1ll11ll11l1_opy_ = (
                                            l1ll11ll1lll_opy_.SubElement(
                                                l1l1lllll1ll_opy_, "beat-unit-dot"
                                            )
                                        )
                                    if l1l111l1l1_opy_.l1l11l1lll_opy_ != "no":
                                        l1ll1ll11l1l_opy_ = (
                                            l1ll11ll1lll_opy_.SubElement(
                                                l1l1lllll1ll_opy_, "per-minute"
                                            ).text
                                        ) = (l1l111l1l1_opy_.l1l11l1lll_opy_)
                                if l1l111l1l1_opy_.t == "sound":
                                    l1ll1ll1ll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1l1llll1_opy_, "sound"
                                    )
                                    if l1l111l1l1_opy_.l1l1l1111l_opy_ != "no":
                                        l1ll1ll1ll1l_opy_.attrib = {
                                            "tempo": l1l111l1l1_opy_.l1l1l1111l_opy_
                                        }
                                    if l1l111l1l1_opy_.l11l111l1l1_opy_ != "no":
                                        l1ll1ll1ll1l_opy_.attrib = {
                                            "tempo": l1l111l1l1_opy_.l11l111l1l1_opy_
                                        }
                                if l1l111l1l1_opy_.t == "words":
                                    l1ll1111111l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1l1llll1_opy_, "direction-type"
                                    )
                                    l1ll11l1ll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                        l1ll1111111l_opy_, "words"
                                    ).text = l1l111l1l1_opy_.words
                            if event.l11l1111ll1_opy_ != 1:
                                l1ll1l1lll11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1l1llll1_opy_, "staff"
                                ).text = str(event.l11l1111ll1_opy_)
                        elif event.t == "backup":
                            l1ll1l1111l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                l1ll111111l1_opy_, "backup"
                            )
                            l1ll1l1lllll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                l1ll1l1111l1_opy_, "duration"
                            ).text = str(event.l1l1111l11_opy_)
                        elif event.t == "barline":
                            l1ll1l111l11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                l1ll111111l1_opy_, "barline"
                            )
                            if event.location != "no":
                                l1ll1l111l11_opy_.attrib = {"location": event.location}
                            if event.l1111llll1l_opy_ != "no":
                                l1ll11lll1ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1l111l11_opy_, "bar-style"
                                ).text = event.l1111llll1l_opy_
                            if event.l111l1ll11l_opy_:
                                l1ll11l11111_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1l111l11_opy_, "ending"
                                )
                                if event.l11l11ll1l1_opy_ != "no":
                                    l1ll11l11111_opy_.attrib = {
                                        "number": event.l11l11ll1l1_opy_
                                    }
                                if event.l11l1111l11_opy_ != "no":
                                    l1ll11l11111_opy_.attrib.update(
                                        {"type": event.l11l1111l11_opy_}
                                    )
                            if event.l11l11l11l1_opy_ != "no":
                                l1l1llll1l11_opy_ = l1ll11ll1lll_opy_.SubElement(
                                    l1ll1l111l11_opy_, "repeat"
                                )
                                l1l1llll1l11_opy_.attrib = {
                                    "direction": event.l11l11l11l1_opy_
                                }
                        elif event.t == "print":
                            l1l1lllllll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                l1ll111111l1_opy_, "print"
                            )
                            if event.l111l111lll_opy_ != "no":
                                l1l1lllllll1_opy_.attrib = {
                                    "new-system": event.l111l111lll_opy_
                                }
                        elif event.t == "sound":
                            print("model to xml sound")
                            l1ll1ll1ll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                                l1ll111111l1_opy_, "sound"
                            )
                            if event.l1l1l1111l_opy_ != "no":
                                l1ll1ll1ll1l_opy_.attrib = {
                                    "tempo": event.l1l1l1111l_opy_
                                }
                            if event.l11l111l1l1_opy_ != "no":
                                l1ll1ll1ll1l_opy_.attrib = {
                                    "tempo": event.l11l111l1l1_opy_
                                }
                        elif l1l11l1ll_opy_ and event.t == "karaoke":
                            l1l1llll11l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                                l1ll111111l1_opy_, "karaoke"
                            ).text = event.l1l1l1l1l1_opy_
            elif element.t == "part-list":
                l1l1lll1ll11_opy_ = l1ll11ll1lll_opy_.SubElement(root, "part-list")
                for l1llll111ll1_opy_ in element.l1l1l1lll1_opy_:
                    l1ll11l1ll11_opy_ = l1ll11ll1lll_opy_.SubElement(
                        l1l1lll1ll11_opy_, "score-part"
                    )
                    if l1llll111ll1_opy_.l111ll1ll1l_opy_ != "no":
                        l1ll11l1ll11_opy_.attrib = {
                            "id": l1llll111ll1_opy_.l111ll1ll1l_opy_
                        }
                    if l1llll111ll1_opy_.l111l1lll11_opy_ != "no":
                        l1l1lllll1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11l1ll11_opy_, "part-name"
                        ).text = l1llll111ll1_opy_.l111l1lll11_opy_
                    if l1llll111ll1_opy_.l11l1111lll_opy_ != "no":
                        l1ll1l11lll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11l1ll11_opy_, "part-abbreviation"
                        ).text = l1llll111ll1_opy_.l11l1111lll_opy_
                    if l1llll111ll1_opy_.l111l1l1lll_opy_ != "no":
                        l1ll11ll11ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11l1ll11_opy_, "score-instrument"
                        )
                        l1ll11ll11ll_opy_.attrib = {
                            "id": l1llll111ll1_opy_.l111l1l1lll_opy_
                        }
                    if l1llll111ll1_opy_.l111ll11l11_opy_ != "no":
                        l1ll11l1l1ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11ll11ll_opy_, "instrument-name"
                        ).text = l1llll111ll1_opy_.l111ll11l11_opy_
                    if (
                        l1llll111ll1_opy_.l11l11111l1_opy_ != "no"
                        or l1llll111ll1_opy_.l11l1111l1l_opy_ != "no"
                    ):
                        l1ll11llllll_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11l1ll11_opy_, "midi-device"
                        )
                        l1ll11llllll_opy_.attrib = {
                            "id": l1llll111ll1_opy_.l11l11111l1_opy_,
                            "port": l1llll111ll1_opy_.l11l1111l1l_opy_,
                        }
                    if l1llll111ll1_opy_.l1111l1l11l_opy_ != "no":
                        l1ll11ll1111_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11l1ll11_opy_, "midi-instrument"
                        )
                        l1ll11ll1111_opy_.attrib = {
                            "id": l1llll111ll1_opy_.l1111l1l11l_opy_
                        }
                    if l1llll111ll1_opy_.l1l11l11ll_opy_ != "no":
                        l1l1llll11ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11ll1111_opy_, "midi-channel"
                        ).text = l1llll111ll1_opy_.l1l11l11ll_opy_
                    if l1llll111ll1_opy_.l1l1l11l11_opy_ != "no":
                        l1ll111ll1ll_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11ll1111_opy_, "midi-program"
                        ).text = l1llll111ll1_opy_.l1l1l11l11_opy_
                    if l1llll111ll1_opy_.l1l1111111_opy_ != "no":
                        l1ll1ll11ll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11ll1111_opy_, "volume"
                        ).text = l1llll111ll1_opy_.l1l1111111_opy_
                    if l1llll111ll1_opy_.l1111l1lll1_opy_ != "no":
                        l1l1lllll111_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11ll1111_opy_, "pan"
                        ).text = l1llll111ll1_opy_.l1111l1lll1_opy_
                    if l1llll111ll1_opy_.l1llllll1ll_opy_ == True:
                        l1l1lllll11l_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11l1ll11_opy_, "braille-ascending-chords"
                        ).text = "1"
                    elif l1llll111ll1_opy_.l1llllll1ll_opy_ == False:
                        l1l1lllll11l_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11l1ll11_opy_, "braille-ascending-chords"
                        ).text = "-1"
                    else:
                        l1l1lllll11l_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11l1ll11_opy_, "braille-ascending-chords"
                        ).text = l1llll111ll1_opy_.l1llllll1ll_opy_
            elif element.t == "credit":
                l1ll11l11l11_opy_ = l1ll11ll1lll_opy_.SubElement(root, "credit")
                l1ll11l11l11_opy_.attrib = {"page": "1"}
                if element.l111l1l1111_opy_ != "no":
                    l1ll11l1lll1_opy_ = l1ll11ll1lll_opy_.SubElement(
                        l1ll11l11l11_opy_, "credit-type"
                    ).text = element.l111l1l1111_opy_
                l1ll1l1ll1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                    l1ll11l11l11_opy_, "credit-words"
                ).text = element.l111ll1l1l1_opy_
            elif element.t == "work":
                if not l1ll1111ll11_opy_ and not l1ll1l1l1ll1_opy_:
                    l1ll1l1l1111_opy_ = l1ll11ll1lll_opy_.SubElement(root, "work")
                if element.l111ll111ll_opy_ != "no":
                    l1ll1111ll11_opy_ = True
                    l111ll111ll_opy_ = element.l111ll111ll_opy_
                if element.l111l11l111_opy_ != "no":
                    l1ll1l1l1ll1_opy_ = True
                    l111l11l111_opy_ = element.l111l11l111_opy_
            elif l1l11l1ll_opy_ and element.t == "braille-global":
                l1l1llllllll_opy_ = l1ll11ll1lll_opy_.SubElement(root, "braille-global")
                for event in element.l111ll1l11l_opy_:
                    if event.t == "global-key":
                        l1ll11lll1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1l1llllllll_opy_, "global-key"
                        )
                        l1ll1ll11l11_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll11lll1l1_opy_, "global-fifths"
                        ).text = str(event.l11l11l111l_opy_)
                    if event.t == "global-time":
                        l1ll111lll1l_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1l1llllllll_opy_, "global-time"
                        )
                        l1ll111ll1l1_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll111lll1l_opy_, "global-beats"
                        ).text = event.l1111ll1111_opy_
                        l1ll1111l111_opy_ = l1ll11ll1lll_opy_.SubElement(
                            l1ll111lll1l_opy_, "global-beat-type"
                        ).text = event.l1111ll11l1_opy_
                        if event.l1111lll1l1_opy_ != "no":
                            l1ll111lll1l_opy_.attrib = {
                                "symbol": event.l1111lll1l1_opy_
                            }
        if l1ll1111ll11_opy_:
            l1l1llll1111_opy_ = l1ll11ll1lll_opy_.SubElement(
                l1ll1l1l1111_opy_, "work-number"
            ).text = l111ll111ll_opy_
        if l1ll1l1l1ll1_opy_:
            l1l1llll1lll_opy_ = l1ll11ll1lll_opy_.SubElement(
                l1ll1l1l1111_opy_, "work-title"
            ).text = l111l11l111_opy_
        l1l1lll1llll_opy_ = minidom.parseString(
            l1ll11ll1lll_opy_.tostring(root)
        ).toprettyxml(indent="   ", encoding="UTF-8", standalone="")
        if l11l1l111l_opy_:
            self._1l11l11l_opy_(str(l1l1lll1llll_opy_))
        self._1l1l1lll_opy_(l1l1lll1llll_opy_)
        l11l1l11l1_opy_ = time.time()
        if l1l11l1ll_opy_:
            print("temps model to bxml", l11l1l11l1_opy_ - t1)
        else:
            print("temps model to musicxml", l11l1l11l1_opy_ - t1)