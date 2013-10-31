SELECT 
  public.broadcaster.name, public.program.name,public.epg_event.descriptor 
FROM 
  public.epg_event, 
  public.program, 
  public.broadcaster
WHERE 
  program.id = epg_event.program AND broadcaster.id = program.broadcaster AND
  broadcaster.name = 'SBT';
