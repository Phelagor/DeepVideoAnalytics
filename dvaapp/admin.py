from django.contrib import admin
from .models import Video, Frame, TEvent, IndexEntries, QueryResults, DVAPQL, VDNServer,\
    LOPQCodes, Region, Tube, Detector, Segment, DeletedVideo, \
    VideoLabel, FrameLabel, RegionLabel, TubeLabel, SegmentLabel, Label, ManagementAction, \
    StoredDVAPQL, Analyzer, Indexer, Retriever, SystemState


@admin.register(SystemState)
class SystemStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoLabel)
class VideoLabelAdmin(admin.ModelAdmin):
    pass


@admin.register(FrameLabel)
class FrameLabelAdmin(admin.ModelAdmin):
    pass


@admin.register(SegmentLabel)
class SegmentLabelAdmin(admin.ModelAdmin):
    pass


@admin.register(RegionLabel)
class RegionLabelAdmin(admin.ModelAdmin):
    pass


@admin.register(TubeLabel)
class TubeLabelAdmin(admin.ModelAdmin):
    pass


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(DeletedVideo)
class DeletedVideoAdmin(admin.ModelAdmin):
    pass


@admin.register(QueryResults)
class QueryResultsAdmin(admin.ModelAdmin):
    pass


@admin.register(DVAPQL)
class DVAPQLAdmin(admin.ModelAdmin):
    pass

@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    pass


@admin.register(IndexEntries)
class IndexEntriesAdmin(admin.ModelAdmin):
    pass


@admin.register(VDNServer)
class VDNServerAdmin(admin.ModelAdmin):
    pass


@admin.register(TEvent)
class TEventAdmin(admin.ModelAdmin):
    pass


@admin.register(LOPQCodes)
class LOPQCodesAdmin(admin.ModelAdmin):
    pass


@admin.register(Tube)
class TubeAdmin(admin.ModelAdmin):
    pass


@admin.register(Detector)
class DetectorAdmin(admin.ModelAdmin):
    pass


@admin.register(Analyzer)
class AnalyzerAdmin(admin.ModelAdmin):
    pass


@admin.register(Indexer)
class IndexerAdmin(admin.ModelAdmin):
    pass


@admin.register(Retriever)
class RetrieverAdmin(admin.ModelAdmin):
    pass


@admin.register(ManagementAction)
class ManagementActionAdmin(admin.ModelAdmin):
    pass


@admin.register(StoredDVAPQL)
class StoredDVAPQLAdmin(admin.ModelAdmin):
    pass
