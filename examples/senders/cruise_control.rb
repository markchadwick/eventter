class EventterLogger
  def initialize(project)
  end

  def build_failed(error)
    `python ./cruise_control.py Failed "${error}"`
  end
  
  def build_fixed(message)
    `python ./cruise_control.py Fixed "${error}"`
  end
end

Project.plugin :eventter_logger
