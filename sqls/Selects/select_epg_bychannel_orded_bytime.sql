SELECT 
  epg_event.startdate, epg_event.starttime, broadcaster.name, program.name, epg_event.descriptor
FROM 
  public.epg_event, 
  public.program, 
  public.broadcaster
WHERE 
  program.id = epg_event.program AND broadcaster.id = program.broadcaster AND
  broadcaster.name = 'Globo' AND
  epg_event.startdate = '29/10/2013'
ORDER BY
  epg_event.starttime	
