# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/node/port/SubjectIDList.0.1.dsdl
#
# Generated at:  2022-05-18 08:59:57.416329 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.port.SubjectIDList
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.node.port
import uavcan.primitive


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class SubjectIDList_0_1:
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
    CAPACITY: int = 8192

    def __init__(self, *,
                 mask:        None | _NDArray_[_np_.bool_] | list[bool] = None,
                 sparse_list: None | _NDArray_[_np_.object_] | list[uavcan.node.port.SubjectID_1_0] = None,
                 total:       None | uavcan.primitive.Empty_1_0 = None) -> None:
        """
        uavcan.node.port.SubjectIDList.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        If no parameters are provided, the first field will be default-initialized and selected.
        If one parameter is provided, it will be used to initialize and select the field under the same name.
        If more than one parameter is provided, a ValueError will be raised.
        :param mask:        saturated bool[8192] mask
        :param sparse_list: uavcan.node.port.SubjectID.1.0[<=255] sparse_list
        :param total:       uavcan.primitive.Empty.1.0 total
        """
        self._mask:        None | _NDArray_[_np_.bool_] = None
        self._sparse_list: None | _NDArray_[_np_.object_] = None
        self._total:       None | uavcan.primitive.Empty_1_0 = None
        _init_cnt_: int = 0

        if mask is not None:
            _init_cnt_ += 1
            self.mask = mask  # type: ignore

        if sparse_list is not None:
            _init_cnt_ += 1
            self.sparse_list = sparse_list  # type: ignore

        if total is not None:
            _init_cnt_ += 1
            self.total = total  # type: ignore

        if _init_cnt_ == 0:
            self.mask = _np_.zeros(8192, _np_.bool_)  # Default initialization
        elif _init_cnt_ == 1:
            pass  # A value is already assigned, nothing to do
        else:
            raise ValueError(f'Union cannot hold values of more than one field')

    @property
    def mask(self) -> None | _NDArray_[_np_.bool_]:
        """
        saturated bool[8192] mask
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._mask

    @mask.setter
    def mask(self, x: _NDArray_[_np_.bool_] | list[bool]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.bool_ and x.ndim == 1 and x.size == 8192:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._mask = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.bool_).flatten()
            if not x.size == 8192:  # Length cannot be checked before casting and flattening
                raise ValueError(f'mask: invalid array length: not {x.size} == 8192')
            self._mask = x
        assert isinstance(self._mask, _np_.ndarray)
        assert self._mask.dtype == _np_.bool_  # type: ignore
        assert self._mask.ndim == 1
        assert len(self._mask) == 8192
        self._sparse_list = None
        self._total = None

    @property
    def sparse_list(self) -> None | _NDArray_[_np_.object_]:
        """
        uavcan.node.port.SubjectID.1.0[<=255] sparse_list
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._sparse_list

    @sparse_list.setter
    def sparse_list(self, x: _NDArray_[_np_.object_] | list[uavcan.node.port.SubjectID_1_0]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.object_ and x.ndim == 1 and x.size <= 255:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._sparse_list = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.object_).flatten()
            if not x.size <= 255:  # Length cannot be checked before casting and flattening
                raise ValueError(f'sparse_list: invalid array length: not {x.size} <= 255')
            self._sparse_list = x
        assert isinstance(self._sparse_list, _np_.ndarray)
        assert self._sparse_list.dtype == _np_.object_  # type: ignore
        assert self._sparse_list.ndim == 1
        assert len(self._sparse_list) <= 255
        self._mask = None
        self._total = None

    @property
    def total(self) -> None | uavcan.primitive.Empty_1_0:
        """
        uavcan.primitive.Empty.1.0 total
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._total

    @total.setter
    def total(self, x: uavcan.primitive.Empty_1_0) -> None:
        if isinstance(x, uavcan.primitive.Empty_1_0):
            self._total = x
        else:
            raise ValueError(f'total: expected uavcan.primitive.Empty_1_0 got {type(x).__name__}')
        self._mask = None
        self._sparse_list = None

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if self.mask is not None:  # Union tag 0
            _ser_.add_aligned_u8(0)
            assert len(self.mask) == 8192, 'self.mask: saturated bool[8192]'
            _ser_.add_aligned_array_of_bits(self.mask)
        elif self.sparse_list is not None:  # Union tag 1
            _ser_.add_aligned_u8(1)
            _ser_.pad_to_alignment(8)
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.sparse_list) <= 255, 'self.sparse_list: uavcan.node.port.SubjectID.1.0[<=255]'
            _ser_.add_aligned_u8(len(self.sparse_list))
            for _elem0_ in self.sparse_list:
                _ser_.pad_to_alignment(8)
                _elem0_._serialize_(_ser_)
                assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
        elif self.total is not None:  # Union tag 2
            _ser_.add_aligned_u8(2)
            _ser_.pad_to_alignment(8)
            self.total._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        else:
            raise RuntimeError('Malformed union uavcan.node.port.SubjectIDList.0.1')
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8200, \
            'Bad serialization of uavcan.node.port.SubjectIDList.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> SubjectIDList_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        _tag0_ = _des_.fetch_aligned_u8()
        if _tag0_ == 0:
            _uni0_ = _des_.fetch_aligned_array_of_bits(8192)
            assert len(_uni0_) == 8192, 'saturated bool[8192]'
            self = SubjectIDList_0_1(mask=_uni0_)
        elif _tag0_ == 1:
            _des_.pad_to_alignment(8)
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u8()
            assert _len0_ >= 0
            if _len0_ > 255:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 255')
            _uni1_ = _np_.empty(_len0_, _np_.object_)  # type: ignore
            for _i0_ in range(_len0_):
                _des_.pad_to_alignment(8)
                _e0_ = uavcan.node.port.SubjectID_1_0._deserialize_(_des_)
                assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
                _uni1_[_i0_] = _e0_
            assert len(_uni1_) <= 255, 'uavcan.node.port.SubjectID.1.0[<=255]'
            _des_.pad_to_alignment(8)
            self = SubjectIDList_0_1(sparse_list=_uni1_)
        elif _tag0_ == 2:
            _des_.pad_to_alignment(8)
            _uni2_ = uavcan.primitive.Empty_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = SubjectIDList_0_1(total=_uni2_)
        else:
            raise _des_.FormatError(f'uavcan.node.port.SubjectIDList.0.1: Union tag value {_tag0_} is invalid')
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8200, \
            'Bad deserialization of uavcan.node.port.SubjectIDList.0.1'
        assert isinstance(self, SubjectIDList_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = '(MALFORMED UNION)'
        if self.mask is not None:
            _o_0_ = 'mask=%s' % _np_.array2string(self.mask, separator=',', edgeitems=10, threshold=100, max_line_width=1000000)
        if self.sparse_list is not None:
            _o_0_ = 'sparse_list=%s' % _np_.array2string(self.sparse_list, separator=',', edgeitems=10, threshold=100, max_line_width=1000000)
        if self.total is not None:
            _o_0_ = 'total=%s' % self.total
        return f'uavcan.node.port.SubjectIDList.0.1({_o_0_})'

    _EXTENT_BYTES_ = 4097

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8jkSbg0{^9$`)?H26~~XkkF|}#;9yA7z-^m{A@&lJCI$LPjlq&TS>l3;sQMV)-MQX7W_D&e_m1&Kr8R9+Vd+X)iJSkfQl(1$'
        'u~L4i+TYT1XO6v(?2;df1mD@YkGXRmpL2$T@h=z7Lh;93PTPSBqN=Y%7V;?kjMpPk^&3emO;o6bHFI}F6t?g(*lwr7zOYxG*{62N'
        'O!{FQi_A(e(+}e?iTj5q{Ft|J`K6riHF#W&lR#9{B-7Ogd3{$j^yZz9L#3^$_<JH#xZdqF^(kGyupW40f3?r7nf1BWSy<1tQ1&;t'
        '^@uYc&$4D>BNS24J<N<BaLs+~PH0{qu{_Io+nQH4!hI2ZEaIk?YwlM6Yt8v05-kyH+HAyG(#)AG+`}2Ox056ie84=jem&HFR6NFd'
        'V|c;_SK4o(m8`sM7PpQzaLcOeI978*&McqX`*=)WX&whW3wk#?%<E<vcS?C9)NNY>X2$(`q^x=S=$zfzcw{~J+nQ6iLtVc81N=$n'
        'H7ETfwT6w_M73M>BnlhWEYw6RK`Ur<;wP!dxK6U(m}$rm9V6d2=kAMC=y3SF6aHg&czFXSp1GGt5zpF#vv9LL9_7M*VVAtIj;iCk'
        'kNd4Krq^!q{o-oM88weMF7d|PT<9n?x7bg4T!h-ayzUmu88hDE>aoSOL4vRHXj=*v#(~&pnMgCC(Cdn6cQe4ta3>TQD~?cQ+gUEy'
        '$_k@t*K#F-D%;?ZDsJ<7c{eWZTYT90@=fJM`Kr0_DaY8sxEU37@)D-T+ykBE4V`DAe{9CQHaf+uJS9(iV;;Cnl4mh{dY*jQEIdRL'
        'G-DBL##%H**1z+c-kf|(UXfQ13+qgj=9ZoT_XZ25vYx~)3UznMMfuy|i%-_p9^q11m$%IuM`46MKzlhS^kq!tei1%AI@%Z4Oz&j8'
        ';qGEAS2pMx$IbYS)tjr<<%DyhFbh4j@ayf8Lhe9Z{z`^Y<d}Mab7zAi((Iu*?eDmZ_nqPVFtGQ`Szjf2)(|)l2|wkSSZ2ye6xOYo'
        '-a;_$Z@IfKFjU8`;TdG&P<J8?t(jSGr;<l^Fby1P@;au4pNS?$AU?0lA$*U?(r>ulc@D)L!J2c&-m9)w->W)PS?zLu!Ixa&c`}C|'
        '<jr2#5cUxLaf4Q@;1cGdHsf(qD26jxAa+7@FsrwV&{e5uVB|Im3s<dNme)!XUzZ<{=Zd7;;z1C`&2OY8j($Wwak(^yd4~i~%h}ee'
        'ptJ9I^YSkK-FWH}v&=Z}1nJ2#TfK4mJwd-GosM_BDW@koUWLY|olbSU8K;vSZ`SEV$2&#y=bWDGc&BOI8QO22)}M7c-|^0oE|9)L'
        'dY*KV^aANc(pO1eBYmCpJEU)rULw6r%1FOU`aRO`lfFs%7U|oh?~pE$ULn0o`Y!1*=?ZC;^cv}Vq^qRYN#7^^0qF;%ACmr%^aklo'
        '(p#iIBK<MxPe^}C`Vr~RO3mdaU6hP{*ZbO>J1QMJu1J@4v<Dj%#Kt?`n9FE+^*OE?5u)djJ}!sjp|!@9L04)pS6t7~7qk@&+P<wW'
        '+;{o%vVt_}KQ0Q2_cbmsMUaEMTl?yai}IsjRdN$+iBN8|f}{T(GD?+ZR$&?|;YY3o!VKnX%w4i%r>D5MV#75<M6kMGu5@5IQd;o9'
        '&2!o8>J<xjSSu;l_7|rT07Hw;_Hpr8q~dYR-|F2~ioL^N;gC6+@5!OuzbD)B_e=7r{Db_XJdn@ipUiX*yiXU)`^hDr9~S5z>d7yL'
        'f(4w9z9gQYsqyb<p1=T4fOrDL6BytL5Kn-30>l#_o&fO#h$k?>6Cj=d@dSt`Ks*8B2@p?!cml)|Af5p61c)a<JOSbf5Kn-30>l#_'
        'o&fO#h$lci0pbY|Pk?v=#1kN%0PzHfCqO&_;t3E>fOrDL6Cj=d@dSt`Ks*8B2@p?!cml)|Af5p61c)a<JOSbf5Kn-30!KW7&T%G9'
        '=tN_ufH`z)t*mZ5!jw@(>sHjcxLM{AkD_lRM;N=jDv~1@(!$J_EzI-cNtN}rt+n;d?O#$KBO{7e`MaVEx!&zUT(T_5pUXx0Z&};@'
        'WDG$5XZIn>?l174d_*3}Kg++E#lFuY%%atSJbH8!x9H+RmD79QtU7bt1N6+m=75EYVJqDf%S<Ks;?6Xj746T83O^GJ`}zVYPm(+e'
        'kS>n}nhqB^MzbK?!NwtvG}8%_`0)|p_VEmMa7DMY(s12i#*1!4wUJXTh22QPus3jBUg3mg_C#Qlob2IonSPQmv5!kwk`}GqEj*11'
        'TPbe5M=kM6Su2XyU7o>*x+%S0E?i5l7DP;eUzF{E_dfEpIpb^Id`a#3+e@lWmsQ<+|0t*Z^INOTT=A7WSX;`4AIiV)PNHAS;^9gQ'
        'e*GZu1}aLWd-E8M1NY0ckh93|`Lf|(lr@Y#7kK|iT<-oFCmhG%u8+U)%L=`RQD<wF1G9)-b@~4UnJ=+Kp$uA=eT#KRS(5cz@?UiI'
        'Rc&m3plVc#&p@(Z<zQ5CW;nWZFuXWd{|7>tI*=X_000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
