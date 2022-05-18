# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/file/Path.2.0.dsdl
#
# Generated at:  2022-05-06 20:35:06.503294 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.file.Path
# Version:       2.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Path_2_0:
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
    SEPARATOR:  int = 47
    MAX_LENGTH: int = 255

    def __init__(self,
                 path: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.file.Path.2.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param path: saturated uint8[<=255] path
        """
        self._path: _NDArray_[_np_.uint8]

        if path is None:
            self.path = _np_.array([], _np_.uint8)
        else:
            path = path.encode() if isinstance(path, str) else path  # Implicit string encoding
            if isinstance(path, (bytes, bytearray)) and len(path) <= 255:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._path = _np_.frombuffer(path, _np_.uint8)  # type: ignore
            elif isinstance(path, _np_.ndarray) and path.dtype == _np_.uint8 and path.ndim == 1 and path.size <= 255:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._path = path
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                path = _np_.array(path, _np_.uint8).flatten()
                if not path.size <= 255:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'path: invalid array length: not {path.size} <= 255')
                self._path = path
            assert isinstance(self._path, _np_.ndarray)
            assert self._path.dtype == _np_.uint8  # type: ignore
            assert self._path.ndim == 1
            assert len(self._path) <= 255

    @property
    def path(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=255] path
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .path.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._path

    @path.setter
    def path(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 255:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._path = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 255:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._path = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 255:  # Length cannot be checked before casting and flattening
                raise ValueError(f'path: invalid array length: not {x.size} <= 255')
            self._path = x
        assert isinstance(self._path, _np_.ndarray)
        assert self._path.dtype == _np_.uint8  # type: ignore
        assert self._path.ndim == 1
        assert len(self._path) <= 255

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.path) <= 255, 'self.path: saturated uint8[<=255]'
        _ser_.add_aligned_u8(len(self.path))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.path)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2048, \
            'Bad serialization of uavcan.file.Path.2.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Path_2_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "path"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 255:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 255')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f0_) <= 255, 'saturated uint8[<=255]'
        self = Path_2_0(
            path=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2048, \
            'Bad deserialization of uavcan.file.Path.2.0'
        assert isinstance(self, Path_2_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'path=%s' % repr(bytes(self.path))[1:],
        ])
        return f'uavcan.file.Path.2.0({_o_0_})'

    _EXTENT_BYTES_ = 256

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8dWLmk0{?|o-)|d55O&g}aa`I`0#xFMx{3ff5?oLqQ1OHb4Inp(agwSOmDS$e*t_(+ciP)?a!5$@0Ys&hsFda3<L^Mcz|5T!'
        'H*GBZ;=9?IZ)U!k{qC2AKmS^4R6lnsE8{#)0-l3WB2hnyFoA$a=_pHcWx>0v`_>eZEesr#8Tb>w_SpaI+isC-F~akg3o(v_4h9MX'
        'd%{ZZntTi<SE=^0;g;@Ao=<#tzT5cCKlbhl7uFgT78Y{<5W!}YapvXS;<kb$o~Cc{SXjX=)#Tos5pIkqy}Nl&pcO55K@Y9$ko9~o'
        'S2-jw0&ORFGs?+~8Y!#B=&^FBb2Zcuf1@o7!JNmt!b4?wQl<0VCKels-11QxgO_i(*L$Zx6c%jZ*$y2cLycd3-@8|NZiSA8iJt}f'
        'y$IbhB4r{{w)EY9-7AwLJ|J@H;^kX)5%N~IDVbdD&Jm=1m!cPVnB?BQciP?*96PnozkB!67s}S8?c?jDJ$H$xnRjd!NM4S@G*J<f'
        'v;(6Q$+I~Ay$p=7shN^=nMYFLNaaWFwXIY~!h*igm6|3`1Dciv{jcv9Ng_=7g6CyE7D)mA58v)KpXQ<5oRD!Fqi*(v9zq{7uxeIG'
        'kN8L&BefXtd1aJar&tw#Bc*Xj^nh+Ve=oTunre{<ito;mZ{umVS^pO}csS04uJ(Vo2mveF!?E;s8cq4_MG^84-6)q_bPHK^n-+MS'
        'BAE@3#%r#LRMB#rjiW7Bo*Vf))vys@dH+tY)9)PY;rt)S@8y<z`*dhnmVun=I=9x%el-D+oT6jQ^1z6QthhPN?a4EqyZMhl^|V`6'
        'xex!ZnAT3`KEHcs_p5`iC)G%pq>w+lOB<V;XJFt~o)HKhmbKIn=y&pl4CN2fNL}DHivio9&58XJcMY$>F~mGejpZu#yY2?h)51i+'
        'Nt}31=Mw!TD#W$wp~M|ml68W^pIb++WlEYhpDFKJTV*Ci@+IytDNGUKPICi895&{g$`8_Vxz<38r$nfk1R87v9|pv>w{)jhxD+|o'
        'U`S?ASH>y=|3p5x|Ib{bu?sn3GJ*?Q9Y!cDFVQw)R4xM@p+Lk;X?A$9eLG+W5?HE}lHtCqnB{=Lw98E8%;MP~HAg5PEKfu(+3NZ#'
        '!RAU23AnPg(YVG83{ak#O{*xArk2GDDMhG~waJ#GQMD5+9k3&*B1tJ?7$_7!7M4{UwF71?X!QZf!A+`hv1-U!8-iiLR)YZ3VfRc^'
        'j!8U<T=kAO5m%5XXp6+kv=~YR#zZ4gvPjasrQWN~3i=jdF1!e1<dPPXwFv|?b{#>y_F0Ru4_K$BE=v_U=^^zfYG#op!4jn(k*($$'
        'QzmsOfF&I%3=~sVgV}&nwh*<loB~fzCg>L;d-=XxukXReIkmdp6LE}bUQj7K{RBU;S$&M3m*TvroJmOVA0t6PLFoqo00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)