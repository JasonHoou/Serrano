# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Params

import flatbuffers

class Params(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsParams(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Params()
        x.Init(buf, n + offset)
        return x

    # Params
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Params
    def Tensors(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Params
    def TensorsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ParamsStart(builder): builder.StartObject(1)
def ParamsAddTensors(builder, tensors): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(tensors), 0)
def ParamsStartTensorsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ParamsEnd(builder): return builder.EndObject()
