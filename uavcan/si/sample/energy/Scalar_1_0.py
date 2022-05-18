# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/energy/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:08.704873 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.energy.Scalar
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Scalar_1_0:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    def __init__(self,
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 joule:     None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.energy.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param joule:     saturated float32 joule
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._joule:     float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.joule = joule if joule is not None else 0.0  # type: ignore

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def joule(self) -> float:
        """
        saturated float32 joule
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._joule

    @joule.setter
    def joule(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._joule = x
        else:
            raise ValueError(f'joule: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.joule):
            if self.joule > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.joule < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.joule)
        else:
            _ser_.add_aligned_f32(self.joule)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.energy.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "joule"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            joule=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.energy.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'joule=%s' % self.joule,
        ])
        return f'uavcan.si.sample.energy.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e1>&m0{?Ya>uwyk6_#Y{w(>Qy9mh@_I!!F8wI<SPS6-)08&|I3l<~%h>{RH*1I`S!WHq;v97!9XK=Y%81q{#uJOT0ud4xPd'
        'fEI0k27Q8{PmrHIXNI$q99w|&ogoj;IXqYDFDJjaaC)rz$=^(efeu2))m%vy%Fmb=a>w<PC{469yv$E;8kPAbQ~c2|<>j+->GSf>'
        '<zhbR#w>#UYZ=@1S?p-(Xcnb#n#WuXhR&wXLZ-@m#@*#g%OozvSU&x!rJt2_oR0mi{JhNPTxN`tUS_y1{{W(2V$_JM%qQ<j9tMZT'
        'wA_Fh<{Gq6Ow@~FGQVzZGcw}N<}mh!N@DpL4<5mSHehZkrp0Vyi8uw?#W{O?{$+NgN=DMiU9e;RajfMa=D~-t;RCLYyJ*h!q;W$Y'
        '4~!^j53KZ=Hg1#zVCC!irH73mJmze`-UHl1*Zj5oq|7h4U}GFG6&w|Gka=*mxk&md(cDkspv+IYLE@KN|C<;adn7oCv&iF$B-`W&'
        'mnKFqLj>F9BxPFjfM^-}oaiLtgeg#=m>QA@K4U{<4Ez<Raat(Uu7l7-$pLIHN{2f)D=u^}@tEdIL~0W7Z3#XhDObxZO+)E312K09'
        'it#h0P|oNGYRWWkL7<4oiQ<3CAU1G(TP4w<bUg}RC5%L17*{um=DcF^6OgM@xTuT=u&Q<?+^sT2R@z%|3ove%g&9XHO+sS6i*ABH'
        '+hMX-+c(<pt}la2$es+qPVO_X@x4}ykY&<-(p^99Szu>gk{Qx&_qt@rnbJ4Oo{+x4EhviE3>|WZtamDzN6v!X8RU*4dr1}spa?V&'
        'lEpFixz<d{a9EoFi9n>$BWuBJa15-)h;%`#5lN<zt5Of!K?WiS18pFf?@RDkY#@(`ucVgRsV}n;LM}*udE-u>EXIi;_wFtc$b=Yt'
        'sX(946eLBKqQ7ntZwN(-8dEk56IR6-0tKDGsSJPAgo;FH{s5S@U}1<6#&jEme7Rz;Rc!M^M@1YK>KrwrI6zV?7)%TFfx_Jw0z<%w'
        '+9{zB&g3&2NsMJ;Ms+9V#WhP^r#<nOc$<!4J&A?7bfzEoY5(Kj^h>dn-}o(8$@8kKe1o{5H+JG=FLug&%B>74^EaBN!1q%~IBaIe'
        'TEfgHRerLtu}5_CS-7%~s~Yz2SsM29@s$!S(_ZHBeEvuubiHBSU-1@;;)+-k%NaD3fP+#fCmxgs`5AXx?(@LKK)Es~`}uiSCz<j&'
        'Y=qoR8MKRh8X=Tkna@6ip1%JOSD!(98h;lWhe)uAPo%QUTN}d^Vs)2CNts_wGY<;aReX?zsPC}D!X>8a#tP@rS1<%#*j$}eXT?Eh'
        'l?L0{yepUnqp<v4TcG6u1mPe3y5La*K@FHKQ2&X7Zh%h4yoI7>P_Sk%Q9H|3Md%|stC&?vAybSvR$(9@3A4HfR4w384}1tY5Kv>_'
        ')g*!j7g)uZuU-O@pgT2PxT?Wj;7Qc7PPs3)<&ivx0kOj!?8ROPF1pd=$zkh;OPlAv%ly<YrTM7(-sGbs&QG{WTIS?sLi8~55{M6Y'
        '^#R1oHpP#j8ktGd;Ru>?eF5cPir?pFAF=>@;}4hw!`*%s!nhtjzbm?bFBfUA&>jr(w3blPnaqQGMl!~+1_awjVj4#qWD5$V<9KeY'
        'pc58PAWjtYr2U>m953jUU7xn=GZts<dJA!?pmUc06yi)lPa~cz=o!m@7IChi=j{G@#L0rbV&%*uzEaQ&i02A=5%EkxFCm^P=&OjW'
        'f?l@gU$c6zSUp#*oY$?sHxRED^cv!og1(9PT0sfo<$_*Ee6^r&Azmuzj}R{w^liio1$_r`zMwa(T?>fk3%Y3STS7cr&>vene}Z_r'
        'pf|0(%l5vGwfkMf*@CWE`&SXC3);5#ShN1<*!xs*JyFngd#_v8zdd`u+jZROdlr9c@n;s_xA=35zp(g$#rqbwEDDSJ7N1)D(&ASZ'
        'zqa^|#cwTsXYu<QAIywf;&MYQHbk!>?l;6%Lx_ghZ-}Q2@nu7N)ev7d#5WD`Z9{z55Z_xOgV!BQ1ehb(+U=T$jU6V=tT}vdF6Co5'
        'xJIu`cnHqkgHdXZy&Yk45tv+UvG5cGM{EF(m<*qd@8=6^ot1X4z1CS@U+Z<-y<YcrZ*}$7N@umV*6DS+tLwMh-A<>TES37nKf>Dr'
        '&Mt|6!<-R!Q2xKfdGTNIpG<5Vh`W99D{+5Od?<b`sQ5@c5dC~Y!$g>>U-UrKZ~8JnTfgd$cXqLPfU?D7u~qks--#!q*5Z$-Cr8@N'
        'MVQ(+#^M+Dt$em_TQDi`AA%Q3bHxrFhwFtf;v@KtLGM5NurN5%w+Qqtu90aAn6?g?cCdy0U>U>Z{2we>%bp(%000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
